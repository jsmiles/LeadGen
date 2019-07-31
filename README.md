# LeadGen
A tool to help Sales teams generate leads

# Summary
LeadGen is a small tool developed in reaction to a question. Is it possible to automate email generation, for sales lead purposes, with only a set of names and companies. The complication is that different companies use different email format patterns. Some use first.surname@company.com, others use variations on that theme. 

The solution posited here is that you need to generate a reference table, **reference.txt** that contains the patterns for each company. LeadGen will then be able to read an **input.txt** and output to the terminal a formatted list of emails following each companies pattern. 

# Usage
To run do the following:
1. Ensure you have both python and pandas installed
2. `cd` to your local directory that has **leadgen.py** saved
3. In the same directory give your **input.txt**. This should contain three values:
 
  * _firstname_: the first name of the lead
  * _surname_: the surname of the lead
  * _company_: the company they work for

4. Create your version of **reference.txt**. This should contain the following fields:
  * _company_: The company for this reference entry
  * _domain_: The domain this company uses i.e. _@company.net_
  * _pattern_: the email pattern followed by this company. Note: this is just a reference to a particular email format i.e. _firstname.surname_ versus _firstinitial.surname_. The logic is built in a different place.
5. Now you can run the program by running `python leadgen.py`

# Output
You should receive two things in the output
1. A formatted email list for the people and companies who have a match in the lookup table
2. A list of companies for whom no email pattern match could be found in the **reference.txt** document. 

# Future
There are no future development plans. If you require different email patterns it should be easy to extend the _elif_ statements within the __emailgen()__ function to suit your needs. 
