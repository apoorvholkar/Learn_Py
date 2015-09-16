indexValue="12.970,58"

#print indexValue

#print float(indexValue.replace(".","dot").replace(",","comma").replace("dot","").replace("comma","."))

tradeDate = "Thursday, 30/04/2015"

print tradeDate

tradeDate1 = tradeDate[-10:].replace("/","-")

print tradeDate1