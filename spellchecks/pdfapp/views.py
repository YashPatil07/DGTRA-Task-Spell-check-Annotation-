import os
import fitz  # PyMuPDF
from django.shortcuts import render
from django.conf import settings
import language_tool_python

def index(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('pdf_file')
        if uploaded_file:
            # Step 1: Save the uploaded PDF
            pdf_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            with open(pdf_path, 'wb') as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)

            # Step 2: Open the PDF document
            doc = fitz.open(pdf_path)

            # Step 3: Extract text and perform spell-checking
            tool = language_tool_python.LanguageTool('en-US') # if you want to add more language then [tool = language_tool_python.LanguageTool('en-US','fr')]  =>frence
            all_text = ""
            annotations = [] 
            
            for page_number,page in enumerate(doc):
                # page_text = page.get_text("blocks")  # Extract plain text from the page
                # all_text += page_text + "\n"
                page_text_blocks = page.get_text("blocks")  # Returns a list of text blocks
                page_text = "\n".join(block[4] for block in page_text_blocks if len(block) > 4)
                # for block in page_text:
                #     block_text = block[4]  # Extract the actual text content
                #     all_text += block_text + "\n"  # Combine all blocks for full text

                # Check for spelling mistakes
                matches = tool.check(all_text)
                
                for match in matches:
                    if match.ruleIssueType == 'misspelling':
                        word = match.context[match.offsetInContext:match.offsetInContext + match.errorLength]  # Extract the misspelled word
                        correction = match.replacements[0] if match.replacements else None
                        
                        # Find all occurrences of the word in the page
                        found_instances = page.search_for(word)
                        
                        if found_instances:         #Ensure there are results
                            for inst in found_instances:
                                # Add highlight annotation
                                highlight = page.add_highlight_annot(inst)
                                if correction:
                                    # Add the correction as a popup note
                                    highlight.set_info(content=f"Misspelled: {word}. Suggested: {correction}")

                        # Store annotations for reference
                        annotations.append({ "word": word, "correction": correction})

            # Step 4: Save the annotated PDF
            annotated_filename = f"annotated_{uploaded_file.name}"
            annotated_path = os.path.join(settings.MEDIA_ROOT, annotated_filename)
            doc.save(annotated_path, garbage=4, deflate=True)
            doc.close()

            # Step 5: Return the result
            annotated_url = f"{settings.MEDIA_URL}{annotated_filename}"
            return render(request, 'pdfapp/index.html', {
                'annotated_url': annotated_url,
                'annotations': annotations
            })

    return render(request, 'pdfapp/index.html')



