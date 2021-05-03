
from django.shortcuts import render, HttpResponse,redirect
from markdown import markdown
from . import util
from .forms import NewPageform,EditPageform
import random 

def index(request):
    # make response to search get req.
    query = request.GET.get("q", "")
    if query != "":
        return redirect(search, query=query)
    # render the List of Entries
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry_detail(request, title):
    # make response to search get req.
    query = request.GET.get("q", "")
    if query != "":
        return redirect(search, query=query)
    # render the entry details
    entry = util.get_entry(title)
    if entry != None:
        entry = markdown(entry)
    return render(
        request, "encyclopedia/entryDetails.html", {"entryTitle": title, "entry": entry}
    )


def search(request, query):

    # make response to search get req.
    q = request.GET.get("q", "")
    if q != "":
        return redirect(search, query=q)

    if util.get_entry(query) != None:
        return redirect(entry_detail, title=query)
    else:
        entries = util.list_entries()
        resultEntries = []
        for entry in entries:
            if query.lower() in entry.lower():
                resultEntries.append(entry)
        return render(
            request,
            "encyclopedia/searchResults.html",
            {
                "query": query,
                "entries": resultEntries,
                "entriesCount": len(resultEntries),
            },
        )


def createNewPage(request):
    if request.method == "POST" : 
        new_page_form = NewPageform(request.POST)
        if new_page_form.is_valid() : 
            cd = new_page_form.cleaned_data
            entries = [entry.lower() for entry in util.list_entries()]
            if cd["title"].lower() in entries:
                error =  'this Entry is Already exist'
            else:
                util.save_entry(cd["title"] ,cd['description'])
                return redirect(entry_detail , cd["title"])
    else:
        new_page_form = NewPageform()
        error = ""
    return render(
        request,
        "encyclopedia/createNewPage.html",
        {"form": new_page_form, "error" :error  },

    )


def entry_edit(request,title):
    if request.method == 'POST':
        edit_page =EditPageform(request.POST) 
        if edit_page.is_valid() :
            description = edit_page.cleaned_data['description']
            util.save_entry(title ,description)
            return redirect(entry_detail , title)
    else:
        edit_page =EditPageform(initial={'description' : util.get_entry(title)}) 
    return render(request ,"encyclopedia/entryEdit.html",
        {"title":title,"form": edit_page},)

def randomEntry(request):
    entries = util.list_entries()
    randomEntryIndex = random.randint(0 , len(entries)-1)
    print(entries[randomEntryIndex])
    return redirect(entry_detail, title=entries[randomEntryIndex])
