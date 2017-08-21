---
output:
  word_document: default
  html_document: default
---
Geography 30323: Data Analysis & Visualization
---
__Fall 2017__

__Texas Christian University__

__Tuesday/Thursday 11:00-12:20__

__Classroom: Scharbauer 4022__

__Instructor: Dr. Kyle Walker__ (<kyle.walker@tcu.edu>)

Office hours: Thursday 10:00-11:00 or by appointment, SCHAR 2004D

---

### Course overview

Data literacy has emerged as an essential skill of the 21st century workforce across many different professional fields and contexts.  Says Hal Varian, Chief Economist at Google: 

> “The ability to take data – to be able to understand it, to process it, to extract value from it, to visualize it, to communicate it – is going to be a hugely important skill in the next decades, not only at the professional level but even at the elementary level for elementary school kids, for high school kids, for college kids.  Because now we really do have essentially free and ubiquitous data.”  

In this course, you will gain experience with several aspects of the data analysis process.   Course topics will include:  

* Obtaining data from a variety of sources, including databases and the Web;
* Cleaning messy datasets, and converting data between different formats and types;
* Using exploratory data analysis to summarize and generate insights from your data; 
* Producing both static and interactive visualizations to both explore your data and communicate your findings with a wider audience.  

In order to perform these tasks, you will also learn the basics of the Python programming language, which you will use for most of the data analysis activities in this course.  Python has rapidly become one of the most popular languages for working with data and has numerous extensions for data wrangling, data analysis, and data visualization.  

Writing code for data analysis is an essential skill, as it allows you to document your workflow and structure your analyses in a coherent, logical way.  That said, this is not a course in software development, nor is it a programming course _per se_.  Instead, think of Python as a tool you’ll be using to work in more flexible and powerful ways with data; in turn, you’ll be gaining skills in technical computing along the way.  

There are no prerequisites for this course; however, you should bring a curiosity about data and an eagerness to learn new technologies!

### Course format

Course time will be used for lecture, discussion, applied tutorials, and assignment work.  The class will be managed through CoCalc, accessible at <https://cocalc.com/app>, and course materials will be available at the course website repository at <https://github.com/walkerke/geog30323>.  You will submit your assignments and view your grades on the Sage Math Cloud website.  

### Readings

There are two required texts for this course: 

Downey, Allen (2014).  _Think Python: How to Think Like a Computer Scientist_.  Needham, MA: Green Tea Press.   This book is available for free at <http://www.greenteapress.com/thinkpython/thinkpython.pdf>.

Yau, Nathan (2013).  _Data Points: Visualization that Means Something_.  Indianapolis, IN: Wiley.  This book is available for free as an e-book through the TCU Library.  If you would like a hard copy, you can purchase it from Amazon relatively inexpensively: <http://www.amazon.com/Data-Points-Visualization-Means-Something/dp/111846219X>.  

Other course readings are freely available online: 

Waltenburg, Eric, and William McLauchlan: Chs. 2-3 from _Exploratory Data Analysis: A Primer for Undergraduates_.  Available at http://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1003&context=pspubs.  

Wickham, Hadley.  Tidy Data.  _Journal of Statistical Software_ 59(10).  Available at https://www.jstatsoft.org/index.php/jss/article/view/v059i10/v59i10.pdf.  

DiBiase, David. Chapter 1: Data and Information.  In: _The Nature of Geographic Information_.  Available at https://www.e-education.psu.edu/natureofgeoinfo/c1.html.  


### Evaluation

You will complete __three take-home examinations__, which collectively comprise __48 percent of your grade__.  Each examination will be comprised of a structured set of homework problems that test you on the computing and analytical skills you've learned to that point in the course.  Deliverables will be in the form of Jupyter Notebooks that show and describe the work you've done.  Take-home exams will be due on __Sunday, October 15__; __Sunday, November 19__; and __Thursday, December 15__, which is the day of our scheduled final exam.  You'll receive the prompt for the take-home exams 2 weeks prior to their due dates.  

You will also have 12 __weekly assignments__ which in total make up __36 percent of your grade__.  Weekly assignments are assigned each Thursday, and due by the end of the day the following Thursday.  You'll have devoted class time each week to work on the assignments.  

In-class tutorials and participation exercises will constitute the remaining __16 percent__ of your grade. 

__The percentage ranges__ to achieve a specific grade are as follows: 

|Percentage|Grade|
|----------|-----|
|94 and up|A|
|90.00-93.99|A-|
|87.00-89.99|B+|
|83.00-86.99|B|
|80.00-82.99|B-|
|77.00-79.99|C+|
|73.00-76.99|C|
|70.00-72.99|C- or Pass|
|67.00-69.99|D+|
|63.00-66.99|D|
|60.00-62.99|D-|
|Below 60|F|

__I do not negotiate grades with students.__  I will award an incomplete (I) only in the most extreme and exceptional circumstances.  Please notify me as soon as possible if you are in a situation where you feel you require an I.  

The attendance policy for this course corresponds to the official TCU attendance policy, which reads: 

> Regular and punctual class attendance is essential, and no assigned work is summarily excused because of absence, no matter what the cause.

Extensions to deadlines and make-up participation credit will only be permitted in the instance of a __documented illness or emergency__ or a __documented TCU-sanctioned activity__.  



### Course Schedule

|__Week__           |__Topic__             |__Reading__                  |__Assignments__        |
|-------------------|----------------------|-----------------------------|-----------------------|
|Week 1: Aug 22-24  |What is data?         |_Data Points_, Ch.1          |Data journalism |
|Week 2: Aug 29-31  |Programming I|_Think Python_, Chs. 1-2   |Python basics; intro to the Jupyter Notebook| 
|Week 3: Sept 5-7 |Programming II|_Think Python_, Ch. 3         |Functions and modules in Python| 
|Week 4: Sept 14 |Programming III|_Think Python_, Chs. 7-8    |Loops/conditionals/object-oriented programming in Python|
|Week 5: Sept 19-21|Exploratory data analysis I|_Exploratory Data Analysis_, Chs. 2-3|Univariate data analysis| 
|Week 6: Sept 26-28 |Exploratory data analysis II|_Data Points_, Ch. 4|Multivariate exploratory visualization|
|Week 7: Oct 3-5|Data wrangling I|Wickham (2014), "Tidy Data"||
|Week 8: Oct 10-12|Data wrangling II||`pandas`: subsetting, indexing, merging<br/>Exam 1 due __Sunday, October 15__|
|Week 9: Oct 19|Advanced I/O: databases, web, APIs||Wrangling data from APIs|
|Week 10: Oct 24-26|Visualization best practices I|_Data Points_, Ch. 2|Data visualization|
|Week 11: Oct 31-Nov 2|Visualization best practices II|_Data Points_, Ch. 5||
|Week 12: Nov 7-9|Interactive data visualization|_Data Points_, Ch. 6|Interactive visualization|
|Week 13-14: Nov 14-21|Geographic data & visualization|_The Nature of Geographic Information_, Ch. 1|Mapping with CARTO<br/><br/>Exam 2 due __Sunday, November 19__|
|Week 15: Nov 28-30|Data dashboards & data science||Data dashboards with Tableau Public|
|Week 16: Dec 5|Data ethics|Articles TBD|Exam 3 due __Thursday, December 14__


### Software

The main software used in this course is the Anaconda distribution of the Python programming language (version 3.5.3) from Continuum Analytics, which includes over 330 popular Python packages for data analysis, visualization, and scientific computing.  Anaconda is available via CoCalc, which means that you can use it on any computer with an internet connection where you can access your CoCalc account.  If you would like to install a local version of Python on your own computer, Anaconda is completely free and can be installed from this link: <http://continuum.io/downloads>, and works on the most popular operating systems (Windows, Mac OS, Linux).  I’ll show you how to install Anaconda on your own computer in class.  If you prefer to do your work on campus, Anaconda will also be available in our classroom, in the Center for Urban Studies computer lab, SCHAR 2015A, and in the Giga Lab in the library.  Late in the course, we will also be using CARTO and Tableau Public for interactive visualization; CARTO is web-based and free, and Tableau Public can be installed for free and will be available on TCU computers.  

All assignments and tutorials in this course will be completed in the Jupyter Notebook, which is an extension to Python that facilitates interactive computing.  The Jupyter Notebook exemplifies _literate programming_, which refers to a combination of textual description, code, and images/graphics in the same document.  In turn, you’ll use the Jupyter notebook to document your workflow and make your work reproducible.  


### Other issues

__Academic conduct:__

Although attendance is not an explicit part of your course grade, it is necessary to successfully complete the in-class tutorials.  If you have to miss class for a TCU-related event and you know when these events will take place (i.e. athletic competition, musical performance, etc.), give me advance notice so that we can work together to ensure that you remain on track.  Additionally, if you need to miss class for illness or family emergency, please give me documentation and I’ll count the absence as excused.

This course will comply with TCU policies on academic conduct and plagiarism.  The TCU statement on academic misconduct from the Student Handbook (Section 3.4) is below: 

> Academic Misconduct (Sec. 3.4 from the Student Handbook) –Any act that violates the academic integrity of the institution is considered academic misconduct. The procedures used to resolve suspected acts of academic misconduct are available in the offices of Academic Deans and the Office of Campus Life and are listed in detail in the Undergraduate Catalog (Student Policies>Academic Conduct Policy Details; http://www.catalog.tcu.edu/current_year/undergraduate/). Specific examples include, but are not limited to: 
>
* Cheating: Copying from another student’s test paper, laboratory report, other report, or computer files and listings; using, during any academic exercise, material and/or devices not authorized by the person in charge of the test; collaborating with or seeking aid from another student during a test or laboratory without permission; knowingly using, buying, selling, stealing, transporting, or soliciting in its entirety or in part, the contents of a test or other assignment unauthorized for release; substituting for another student or permitting another student to substitute for oneself. 
* Plagiarism: The appropriation, theft, purchase or obtaining by any means another’s work, and the unacknowledged submission or incorporation of that work as one’s own offered for credit. Appropriation includes the quoting or paraphrasing of another’s work without giving credit therefore.  
* Collusion: The unauthorized collaboration with another in preparing work offered for credit. 

In short: please don’t cheat, as it is a very serious offense and you will get caught.  If you are in any way struggling in the course and tempted to cheat, please come talk to me so we can address your issues face to face.  

Finally, the classroom is a place where diversity of opinions and perspectives is not only welcomed, but highly encouraged.  I ask you to always be mindful and respectful of the diversity (broadly defined) of your classmates.  

__Disability statement:__

TCU’s statement on disabilities is as follows:

> Texas Christian University complies with the Americans with Disabilities Act and Section 504 of the Rehabilitation Act of 1973 regarding students with disabilities.  Eligible students seeking accommodations should contact the Coordinator of Student Disabilities Services in the Center for Academic Services located in Sadler Hall, 1010.  Accommodations are not retroactive, therefore, students should contact the Coordinator as soon as possible in the term for which they are seeking accommodations. Further information can be obtained from the Center for Academic Services, TCU Box 297710, Fort Worth, TX 76129, or at (817) 257-6567.

### Statement on use of the syllabus

This syllabus is intended for your use as a guide to assist in your planning for the semester.  I reserve the right to make changes to the syllabus and schedule if necessary.  However, rest assured that if I do make any changes to the syllabus, I will give you plenty of advance notice.  
