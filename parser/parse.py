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
			'title': cols[2].a.text,
			'url': cols[2].a['href'],
		
		})
	for row1 in table.find_all('td', class_="subtext"):
		cols1 = row1.find_all('a', class_='hnuser')
		projects.append({
			'author': cols1[0].text,
		})

	for row2 in table.find_all('span', class_="sitebit comhead"):
		col2 = row2.find_all('span', class_='sitestr')
		projects.append({
			'site': col2[0].text,
		})

	for item in projects:
		print(item)
	




def main():
	parse(get_html('https://news.ycombinator.com/'))

if __name__ == "__main__":
	main()