## Paths finder in URLs
In this script the existence of a path at the end of URL has been checked and the status code of response is returned. This can be used in penetration testing, directory managing and etc.

This script uses two xlsx (Excel) files entitled “URLs” and “Pads” as source and paths. The given paths append to end of URLs and the status code of responses have been retrieved. 

### Requirements
```
pip install requests
pip install xlrd==1.2.0
pip install xlsxwriter
```

### Example
/imghp and /mehdibastani are two paths in Pads.xlsx file and we have added two famous sites as http://google.com and http://github.com into URLs.xlsx. The results will be saved in an Excel file entitled “Results” as follows: 

<table>
<thead>
<tr>
<th align="left">URLs</th>
<th align="center">Status</th>
</tr>
</thead>
  
<tr>
<th align="left">http://google.com/imghp</th>
<th align="center">200</th>
</tr>
 
<tr>
<th align="left">http://google.com/mehdibastani</th>
<th align="center">404</th>
</tr>
 
<tr>
<th align="left">http://github.com/imghp</th>
<th align="center">404</th>
</tr>
 
<tr>
<th align="left">http://github.com/mehdibastani</th>
<th align="center">200</th>
</tr>

</table>

<br>
<b>P.S.:</b> 
Usage of this script for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. The programmer assumes no liability and is not responsible for any misuse or damage caused by this program. Only use for educational purposes.

