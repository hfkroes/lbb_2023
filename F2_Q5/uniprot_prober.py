from Bio import Entrez
import re

#pattern = r"([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})"


# Set up Entrez
Entrez.email = "hector.kroes@usp.br"  # Set your email address here
db = "pmc"

# Set up regular expression pattern
pattern = r"([OPQ][0-9][A-Z0-9]{3}[0-9]\b)"

# Set up a list of PMC IDs
pmc_ids = ['PMC9667682','PMC9658796','PMC9789376','PMC9503559','PMC7888446','PMC9639636','PMC9629082','PMC8835746','PMC8065505','PMC9144352','PMC7081199','PMC9015987','PMC8662305','PMC9558030','PMC9048014','PMC6999090','PMC8106652','PMC8277569','PMC8707499','PMC8725978','PMC7297953','PMC8533766','PMC9175115','PMC9128143','PMC8799556','PMC7235846','PMC8965893','PMC8896083','PMC7536829','PMC7485717','PMC8000579','PMC8004658','PMC8124674','PMC7986597','PMC9832379','PMC7273668','PMC7922581','PMC8395060','PMC9508354','PMC8269014','PMC9826399','PMC8147054','PMC8758994','PMC8888908','PMC8968026','PMC8318780','PMC8194669','PMC6817481','PMC7882683','PMC8264553','PMC8967107','PMC7711264','PMC8022522','PMC9553114','PMC8119882','PMC7306921','PMC9654995','PMC6757416','PMC7401704','PMC8011326','PMC6520591','PMC8910853','PMC7794689','PMC7567506','PMC9227170','PMC6337647','PMC7072452','PMC7765872','PMC6435883','PMC8222499','PMC5788550','PMC8011330','PMC7911444','PMC7987310','PMC7830943','PMC8204103','PMC7831088','PMC7790737','PMC5959957','PMC7554086','PMC6506819','PMC7313026','PMC5824897','PMC6423421','PMC6107789','PMC6457050','PMC7464383','PMC6337699','PMC4769573','PMC6141625','PMC7697665','PMC6678893','PMC7246448','PMC8800723','PMC7555265','PMC5279880','PMC7649713','PMC5579142','PMC7037698','PMC7167735','PMC6367241','PMC6721316','PMC7667696','PMC6393885','PMC5915032','PMC8199792','PMC4691095','PMC5989036','PMC7276794','PMC7140613','PMC6389176','PMC5680523','PMC5356613','PMC6097187','PMC6333462','PMC7111250','PMC5062031','PMC5314895','PMC4937031','PMC6161166','PMC6627106','PMC5405532','PMC6151801','PMC6422311','PMC5566057','PMC7261628','PMC5073117','PMC5454969','PMC4475649','PMC5067323','PMC4586418','PMC5404111','PMC6068445','PMC5327052','PMC4949485','PMC4947127','PMC5177873','PMC7015696','PMC6406450','PMC6908309','PMC4850115','PMC4463186','PMC6506414','PMC5609817','PMC4837186','PMC4417587','PMC7996087','PMC6611466','PMC5390006','PMC6727218','PMC4691177','PMC4546454']

# Retrieve the full text of the articles
search_query = '(alzheimer) AND (uniprot) AND (FIRST_PDATE:[2015-01-01 TO 2022-12-31]) AND (PUB_TYPE:REVIEW)'
search_results = Entrez.read(Entrez.esearch(db="pmc", term=search_query, retmax=10, usehistory="y"))
handle = Entrez.efetch(db="pmc", rettype="full", retmode="xml", retstart=0, retmax=int(search_results["Count"]), webenv=search_results["WebEnv"], query_key=search_results["QueryKey"])
print(handle)

"""
# Loop through all PDF files in the folder and search for the pattern
for file_name in os.listdir('./Papers'):
    if file_name.endswith(".pdf"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "rb") as f:
            pdf_content = f.read()
            text = pdf_content.decode("utf-8", errors="ignore")
            try:
                print(text)
            except:
                pass
            matches = re.findall(pattern, text)
            if matches:
                matches = list(set(matches))
                for i in matches:
                    print(f"{file_name[:-4]},{i}")
"""