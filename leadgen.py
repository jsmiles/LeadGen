import pandas as pd

input = pd.read_csv('input.txt',sep=',')
ref = pd.read_csv('reference.txt',sep=',')

def ref_lookup(company):
    if company in ref.loc[:,'Company'].tolist():
        dom = ref.loc[ref['Company']== f'{company}', 'Domain'].iloc[:]
        pat = ref.loc[ref['Company']== f'{company}', 'Pattern'].iloc[:]
        return dom, pat
    else:
        x = pd.Series(1)
        y = pd.Series(2)
        return x, y

c_list = input.loc[:,'Company'].iloc[:]
c_list = c_list.tolist()

def emailgen():
    EmailList = []
    NoEmailList = []
    for i in c_list:
        d, p = ref_lookup(i)
        d = d.item()
        p = p.item()
        if p == 'p1':
            a = input.loc[input['Company']==i,'firstname'].item()
            b = input.loc[input['Company']==i,'surname'].item()
            EmailList.append(f"{a}.{b}{d}")
        elif p == 'p2':
            a = input.loc[input['Company']==i,'firstname'].item()[0]
            b = input.loc[input['Company']==i,'surname'].item()
            EmailList.append(f"{a}{b}{d}")
        elif p == 'p3':
            a = input.loc[input['Company']==i,'firstname'].item()[0]
            b = input.loc[input['Company']==i,'surname'].item()
            EmailList.append(f"{b}.{a}{d}")
        else:
            NoEmailList.append(i)

    return EmailList, NoEmailList

a, b = emailgen()
for i in a:
    print(f"{i}, ")

print("""
    ABOVE: A list of emails, formatted. Don't forget
    to remove the last trailing comma.

    BELOW: A list of the companies with no lookup
    pattern contained in \'reference.txt\'
    """)
print(b)
