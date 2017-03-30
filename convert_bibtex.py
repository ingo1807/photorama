import numpy as np
import string as str
import bibtexparser

FILENAME = '_bibliography/ref.bib'
OUTFILE = '_includes/test.html'

def write_entry(ar,f):
    #writing the HTML code for each entry
    
    if ar['journal'] == '\mnras':
        journal = 'Monthly Notices of the Royal Astronomical Society'
    elif ar['journal'] == '\apj' or ar['journal'] == 'ApJ' or ar['journal'] == 'APJ':
        journal = 'Astrophysical Journal'
    else: 
        journal = ar['journal']
    
    f.write('<li>')
    f.write('<p style="margin-left: 40px;font-weight: bold">')
    
    try:
        f.write('<a target="_blank" href='+ar['link']+'>'+ar['title']+'</a>'+'   ('+ar['year']+')')
    except KeyError:
        try:
            f.write('<a target="_blank" href='+ar['adsurl']+'>'+ar['title']+'</a>'+'   ('+ar['year']+')')   
        except KeyError:
            f.write(ar['title']+'   ('+ar['year']+')')
        
    f.write('</p> \n')
    f.write('<p style="margin-left: 70px;line-height: 95%;">')
    f.write(ar['author'])
    f.write('<br>')
#     f.write('</p>')
    f.write('<font color="grey">')
    f.write('journal: '+journal+' | volume: '+ar['volume']+' | page: '+ar['pages'])
    f.write('</font>')
    f.write('</p> \n')
    f.write('\n')
    return f 
    


#reading bibtex
with open(FILENAME,'r') as database: 
    data = bibtexparser.load(database)

#output file 
out = open(OUTFILE,'wb') 


Ncite = len(data.entries)
print(Ncite)

print(data.entries[2]['month'])

years = []
for i in range(Ncite):
    years.append(np.int(data.entries[i]['year']))
    
print(years)
sort_years = np.argsort(years)[::-1]
# print(np.argsort(years))

# print(data.entries[2]['link'])

for i in sort_years:
    write_entry(data.entries[i],out)
    