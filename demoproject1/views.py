from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    address={'name':'amit','place':'Earth'}
    return render(request, 'index1.html', address)
def analyzed_text(request):
    inputtext= request.POST.get('text')
    RemovePunc= request.POST.get('removepunc','off')
    CapFirst= request.POST.get('fullcaps','off')
    SpaceRemover=request.POST.get('removespace','off')
    CharCounter= request.POST.get('charcount')

    if inputtext=="":
        return HttpResponse("Please Enter some text ")

    elif RemovePunc=='on' and CapFirst=='on' and SpaceRemover=='on' and CharCounter=='on':
        punc = '''!@#$%^&*(\)_+-={}[];:'"|`<>,.?|/'''
        new_text = ""
        for i in inputtext:
            if i not in punc:
                new_text = new_text + i
        captext = new_text.upper()
        remsptext = ""
        for i in captext:
            if i == " ":
                i = ""
            remsptext = remsptext + i
        noofchars = len(remsptext)
        
        arap = 'After removing all the punctuations, capitalizing all the text and removing all the spaces ' \
               'counting the number of characters'
        output = {'heading_text': arap, 'analyze_text': remsptext,'no_of_char':noofchars}
        return render(request, 'index2.html', output)
    
    elif RemovePunc=='on' and CapFirst=='on' and SpaceRemover=='on':
        punc = '''!@#$%^&*(\)_+-={}[];:'"|`<>,.?|/'''
        new_text = ""
        for i in inputtext:
            if i not in punc:
                new_text = new_text + i
        captext = new_text.upper()
        remsptext = ""
        for i in captext:
            if i == " ":
                i = ""
            remsptext = remsptext + i
        arap = 'After removing all the punctuations, capitalizing all the text and removing all the spaces ' 
        output = {'heading_text': arap, 'analyze_text': remsptext}
        return render(request, 'index2.html', output)


    elif RemovePunc=='on' and CapFirst=='on' and CharCounter=='on':
        punc = '''!@#$%^&*(\)_+-={}[];:`'"|<>,.?|/'''
        new_text = ""
        for i in inputtext:
            if i not in punc:
                new_text = new_text + i
        captext = new_text.upper()
        noofchars=len(captext)
        arap = 'After remove all punctuations and capitalizing all the text, counting the number of characters'
        output = {'heading_text': arap, 'analyze_text': captext, 'no_of_char': noofchars}
        return render(request, 'index2.html', output)
    
    elif RemovePunc=='on' and SpaceRemover=='on' and CharCounter=='on':
        punc = '''!@#$%^&*(\)_+-={}[];:'"|`<>,.?|/'''
        new_text = ""
        for i in inputtext:
            if i not in punc:
                new_text = new_text + i
        remsptext = ""
        for i in new_text:
            if i == " ":
                i = ""
            remsptext = remsptext + i
        noofchars = len(remsptext)
        
        arap = 'After removing all the punctuationsand removing all the spaces counting the number of characters'
        output = {'heading_text': arap, 'analyze_text': remsptext,'no_of_char':noofchars}
        return render(request, 'index2.html', output)

    elif CapFirst=='on' and SpaceRemover=='on' and CharCounter=='on':
        captext = inputtext.upper()
        remsptext = ""
        for i in captext:
            if i == " ":
                i = ""
            remsptext = remsptext + i
        noofchars = len(remsptext)
        arap = 'After capitalizing all the text and removing all the space, counting the number of characters'
        output = {'heading_text': arap, 'analyze_text': remsptext, 'no_of_char': noofchars}
        return render(request, 'index2.html', output)
    
    elif RemovePunc=='on' and CapFirst=='on':
        punc = '''!@#$%^&*(\)_+-={}[];:'"|<>,.`?|/'''
        new_text = ""
        for i in inputtext:
            if i not in punc:
                new_text = new_text + i
        captext = new_text.upper()
        arap = 'After removing all the punctuations and capitalizing the text'
        output = {'heading_text': arap, 'analyze_text': captext}
        return render(request, 'index2.html', output)

    elif RemovePunc=='on' and SpaceRemover=='on':
        punc = '''!@#$%^&*(\)_+-={}[];:'"|<>,.`?|/'''
        new_text = ""
        for i in inputtext:
            if i not in punc:
                new_text = new_text + i
        remsptext=""
        for i in new_text:
            if i==" ":
                i=""
            remsptext=remsptext+i
        arap = 'After removing all the punctuaions and spaces from text '
        output = {'heading_text': arap, 'analyze_text': remsptext}
        return render(request, 'index2.html', output)

    elif RemovePunc=='on' and CharCounter=='on':
        punc = '''!@#$%^&*(\)_+-={}[];:'"`|<>,.?|/'''
        new_text = ""
        for i in inputtext:
            if i not in punc:
                new_text = new_text + i
        noofchars=len(new_text)
        arap = 'After remove all punctuations counting the number of characters'
        output = {'heading_text': arap, 'analyze_text': new_text, 'no_of_char':noofchars}
        return render(request, 'index2.html', output)

    elif CapFirst=='on' and CharCounter=='on':
        captext = inputtext.upper()
        noofchars=len(captext)
        arap = 'After capitalizing all text counting the number of characters'
        output = {'heading_text': arap, 'analyze_text': captext, 'no_of_char': noofchars}
        return render(request, 'index2.html', output)

    elif SpaceRemover == 'on' and CharCounter == 'on':
        remsptext=""
        for i in inputtext:
            if i==" ":
                i=""
            remsptext=remsptext+i
        noofchars=len(remsptext)
        arap = 'After removing all the spaces from text, counting the number of characters'
        output = {'heading_text': arap, 'analyze_text': remsptext, 'no_of_char': noofchars}
        return render(request, 'index2.html', output)

    elif RemovePunc=='on':
        punc= '''!@#$%^&*(\)_+-={}[];:'"|<>,.`?|/'''
        new_text = ""
        for i in inputtext:
            if i not in punc:
                new_text = new_text + i

        arap= 'After remove all punctuations'
        output={'heading_text': arap, 'analyze_text':new_text}
        return render(request, 'index2.html', output)
       


    elif CapFirst=='on':
        captext=inputtext.upper()
        acat='After Capitalize all text '
        output={'heading_text':acat, 'analyze_text':captext}
        return render(request, 'index2.html', output)

    
    elif SpaceRemover=='on':
        remsptext=""
        for i in inputtext:
            if i==" ":
                i=""
            remsptext=remsptext+i

        aras='After Remove all Spaces'
        output={'heading_text':aras, 'analyze_text':remsptext}
        return render(request,'index2.html', output)
    

    elif CharCounter=='on':
        print(inputtext)
        noofchars=len(inputtext)
        acat='After counting all text'
        output={'heading_text':acat, 'analyze_text':noofchars}
        return render(request,'index2.html', output)
    else:
        return render(request,'index2.html')

def about(request):
    return HttpResponse('''<h1 style="text-align:center;">This is Amit Kumar Mallick , The creator of this website .<br> Hope you will enjoy 
    it .<br> Thank you .</h1>''')
def contact_us(request):
    return HttpResponse('''<h1 style="text-align:center;">Contact No : 6370382928 <br> Mail id : amitzqx@gmail.com <br> 
    Github : amit928 
    </h1>''')
