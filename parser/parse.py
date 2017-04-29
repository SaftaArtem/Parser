import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def parse(html):
	soup = BeautifulSoup(html)
	table = soup.find('table', class_="itemlist")
	
	projects = []

	for row in table.find_all('tr', class_="athing"):
		cols = row.find_all('td')
		projects.append({
			'title': cols[2].a.text
		})
	for project in projects:
		print(project)





def main():
	parse(get_html('https://news.ycombinator.com/'))

if __name__ == "__main__":
	main()