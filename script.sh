curl 'https://octopart.com/api/v4/endpoint' 
-H 'Accept-Encoding: gzip, deflate' 
-H 'Content-Type: application/json' 
-H 'Accept: application/json' 
-H 'Connection: keep-alive' 
-H 'DNT: 1' 
-H 'Origin: https://octopart.com' 
-H 'token: be6d8bdd-11a4-4ae0-9337-7b65f6d39c90' 
--data-binary '{"query":"query { 
search(q: \"MFR_PART_NUM\", limit: 1) { 
    results { 
part{ 
 mpn 
   manufacturer { 
       name 
      } 
 sellers(include_brokers: INCL_BROKERS) { 
      company { 
     name 
   } 
   offers { 
        click_url 
         inventory_level 
         updated 
         prices { 
        price 
       currency 
      quantity 
          } 
    } 
     } 
     } 
     } 
     } 
     }" 
}' --compressed --output results.json