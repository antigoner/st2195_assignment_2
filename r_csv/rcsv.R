library(rvest)
library(xml2)
link <- "https://en.wikipedia.org/wiki/Delimiter-separated_values"
dsv_page <- read_html(link)
dsv_table <- html_nodes(dsv_page,xpath='//*[@id="mw-content-text"]/div[1]/pre/text()')
dsv_table
csv_text <- xml_text(dsv_table)
cat(csv_text)
df <- read.csv(text=csv_text)
print(df)
write.csv(df,file=rcsv.dat)
