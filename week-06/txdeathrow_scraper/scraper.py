from bs4 import BeautifulSoup
import data_helper
from format_helper import calc_years_diff
from format_helper import make_absolute_url
from format_helper import txdate_to_iso


def get_inmate_data():
    """
    A convenient wrapper function that wraps up all the other sub/helper
        functions so that the user of the scraper.py script need only
        to invoke this to get the nice and clean data.

        import scraper
        data = scraper.get_data()

    Returns:
        <list>: A list of dict objects, with the dict objects as defined in
            the documentation of the wrangle_inmate_data_from_tag()
            function
    """
    inmaterows = get_and_parse_inmate_rows()
    the_data = []
    for row in inmaterows:
        d = wrangle_inmate_data_from_tag(row)
        the_data.append(d)
    return the_data



def get_and_parse_inmate_rows():
    """
    A convenience function that calls the functions needed to
      fetch the webpage, parse it as HTML, and return a list of bs4 <Tag>
      objects, each one derived from the HTML for a table row
       that ostensibly contains info about a TX death row inmate

    Should call on functionality in the `data_helper.py` script (i.e. get_html())

    Args:
        None

    Returns:
        <list>: A list of bs4.Tag objects, of the <tr> type
    """
    ### Fill in yourself, should be exactly the same
    ### as from the function found in checker.py
    ### of txdeathrow_check exercise

    txt = data_helper.get_html()
    soup = BeautifulSoup(txt, 'lxml')
    tags = soup.select('tr')
    return tags[1:]


def wrangle_inmate_data_from_tag(rowtag):
    """
    Args:
        rowtag: a BeautifulSoup <Tag> object, ostensibly representing a table row
            from a parsed Texas death row HTML table, e.g.

            <tr>
            <td>999608</td>
            <td align="center"><a href="dr_info/hudsonwilliam.html" title="Offender Information for William Hudson">Offender Information</a></td>
            <td>Hudson</td>
            <td>William</td>
            <td>07/03/1982</td>
            <td align="center">M</td>
            <td>White</td>
            <td>11/16/2017</td>
            <td>Anderson</td>
            <td>11/14/2015</td>
            </tr>

    Returns:
        <dict>: A dictionary object that contains some of the values in
            the HTML, with formatting where standardization is needed --
            e.g. for dates and for the inmate's URL (absolute vs relative)
            and some derived attributes, e.g. 'age_at_offense'

            The value for 'url' should be an absolute URL, i.e. a valid
               URL on the Web, not a relative one.

            'birthdate', date_received', 'date_offense' should be in 'YYYY-MM-DD'
                format

            All values are strings except for:
               'age_at_offense', which is an integer derived from birthdate and
                                 date of offense

               'years_before_death_row', which is a float
                              (rounded to nearest tenth) derived
                              from date of offense and date received, i.e.
                              number of years between commission of crime and entering
                              death row.

        e.g.
            {
                'tdcj_id': '999608',
                'url': 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_info/hudsonwilliam.html',
                'last_name': 'Hudson',
                'first_name': 'William',
                'birthdate': '1982-07-03',
                'gender': 'M',
                'race': 'White',
                'date_received': '2017-11-16',
                'date_offense': '2015-11-14',
                'age_at_offence': 33,
                'years_before_death_row': 2.0
            }
    """
    ### fill in yourself
    ### (this one will be pretty long, though it's mostly tedious/repetitive steps)

    offender_dict = {}
    td_elements = rowtag.select('td')
    
    #get id number and add to dictionary
    offender_dict['tdcj_id'] = td_elements[0].text.strip()

    #derive absolute url from relative, file under 'url'
    url_line = rowtag.select('td a')
    relative_url = url_line[0].attrs['href']
    offender_dict['url'] = make_absolute_url(relative_url)

    #get last name, first name
    offender_dict['last_name'] = td_elements[2].text.strip()
    offender_dict['first_name'] = td_elements[3].text.strip()

    #get birthdate (add in 'YYYY-MM-DD' format)
    birthdate = td_elements[4].text.strip()
    iso_birthdate = txdate_to_iso(birthdate)
    offender_dict['birthdate'] = iso_birthdate

    #gender
    gender = td_elements[5].text.strip()
    offender_dict['gender'] = gender

    #race
    race = td_elements[6].text.strip()
    offender_dict['race'] = race

    #get the date sentence received ('YYYY-MM-DD' format)
    date_received = txdate_to_iso(td_elements[7].text)
    offender_dict['date_received'] = date_received

    #get the date of the offense ('YYYY-MM-DD' format)
    date_of_offense = txdate_to_iso(td_elements[-1].text.strip())
    offender_dict['date_offense'] = date_of_offense

    #calculate age at offense and store as integer value
    age = calc_years_diff(iso_birthdate, date_of_offense) + 1
    offender_dict['age_at_offense'] = int(age)

    #determine years before death row
    years_before = calc_years_diff(date_of_offense, date_received)
    offender_dict['years_before_death_row'] = years_before

    #county
    county = td_elements[-2].text.strip()
    offender_dict['county'] = county

    #give you the dictionary with each element
    return offender_dict