import urllib.request
from bs4 import BeautifulSoup
import csv

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

Base_Url = 'https://news.ycombinator.com/'
def parse(html):
	soup = BeautifulSoup(html)
	table = soup.find('table', class_="itemlist")
	author_index = 0
	site_index = 0
	projects = []
	authors = []
	sites = []
	
	te =table.find_all('tr', class_="athing")
	
	for item in te:
		row_span = item.find_all('span', class_='sitestr')
		if row_span == []:
			sites.append('without site')
		else:
			sites.append(row_span[0].text)

	


	author = soup.find_all('td', class_='subtext')
	for item in author:
		authors.append(item.a.text)
	
	for row in table.find_all('tr', class_="athing"):
		cols = row.find_all('td')
		projects.append({
			'title': cols[2].a.text,
			'url': cols[2].a['href'],
			'sites': sites[site_index],
			'author': authors[author_index],
		})
		author_index = author_index+1
		site_index = site_index+1
	return projects

def save(projects, path):
	with open(path, 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(('title', 'url', 'sites', 'author'))

		for project in projects:
			writer.writerow((project['title'], project['url'], project['sites'], project['author']))


def main():
	projects = []
	for page in range(1,100):
		print('Parsing %d%%' %((page/100)*100)) 
		projects.extend(parse(get_html(Base_Url + 'news?p=%d' % page)))
	
	save(projects, 'projects.csv')

if __name__ == "__main__":
	main()