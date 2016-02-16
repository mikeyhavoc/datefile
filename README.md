# datefile
version 1
updates the date on program files.<br>

###imports 
<ul>
<li>datetime</li>
<li>os</li>
</ul>

###file_change
date_name = year-month-day-minute_filename

if file is date.py<br>
  continue  // skip date.py file<br>
if file is .git <br>
  continue // skip .git repository<br>
if file starts with year<br>
  continue // skip previously dated files.<br>
  
rename filesnames, datename

file_change(give directory here)


future project: TODO let you type the directory to rename files.
