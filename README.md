# maize_v3_v4_conversion
usage: v3_v4.py [-h] [-v3] [-v4] [-r] [-o]     

optional arguments:  

  -h, --help         show this help message and exit  
  
  -v3 , --v3gene     v3inputgenelist  
  
  -v4 , --v4gene     v4inputgenelist  
  
  -r , --reference   v3_v4_gramene  
  
  -o , --output      outputfile  
  
 ###########################  
 
 if you want to convert v3 to v4:  
 
 use:  
 
 python v3_v4.py -r v4_v3gramene.txt -v3 <yourv3genelist.txt> -o result.txt  
 
 if you want to convert v4 to v3:  
 
 use:  
 
 python v3_v4.py -r v4_v3gramene.txt -v4 <yourv4genelist.txt> -o result.txt
