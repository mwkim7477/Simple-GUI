"""
Matt Kim
"""

import json
import Tkinter as tk

class MyGUI(object):
    """
    A GUI that displays and modifies data.
    """
    def __init__(self):
        """
        Process data into multiple lists and set up tkinter.
        """
        self.processdata()
        self.initialize_tkinter()

    def initialize_tkinter(self):
        """
        Sets up tkinter.
        """
        self.root = tk.Tk()
        self.root.title("City Information")
        self.root.geometry('200x200')
        self.setup_data_tkinter()
        self.root.mainloop()

    def setup_data_tkinter(self):
        """
        Creates entries, labels, and an OptionMenu
        for the data in tkinter
        """
        self.setup_city()
        self.setup_county()
        self.setup_latitude()
        self.setup_longitude()

    def setup_longitude(self):
        """
        Creates the label for longitude as well as its entry
        """
        longitudelabel = tk.Label(self.root, text="Longitude").grid(row=3)
        self.longitudeentry = tk.Entry(self.root)
        self.longitudeentry.insert(0, self.longitudes[0])
        self.longitudeentry.grid(row=3, column=1)

    def setup_latitude(self):
        """
        Creates the label for latitude as well as its entry
        """
        latitudelabel = tk.Label(self.root, text="Latitude").grid(row=2)
        self.latitudeentry = tk.Entry(self.root)
        self.latitudeentry.insert(0, self.latitudes[0])
        self.latitudeentry.grid(row=2, column=1)

    def setup_county(self):
        """
        Creates the label for county as well as its entry
        """
        countylabel = tk.Label(self.root, text="County").grid(row=1)
        self.countyentry = tk.Entry(self.root)
        self.countyentry.insert(0, self.counties[0] + " County")
        self.countyentry.grid(row=1, column=1)

    def setup_city(self):
        """
        Creates the label as well as the OptionMenu for city
        """
        citylabel = tk.Label(self.root, text="City").grid(row=0)
        cityvar = tk.StringVar()
        cityvar.set(self.cities[0])

        #Trace is used to update all entries
        cityvar.trace('w', lambda name, index, mode, \
                  cityvar=cityvar: self.load_up_selected_data(cityvar))
        citymenu = tk.OptionMenu(self.root, cityvar, *self.cities)
        citymenu.grid(row=0, column=1)

    def processdata(self):
        """
        Separates all data into multiple lists.
        Also ignores all counties that have their own entries
        """
        #Sort based on city name
        myjson = sorted(json.load(open('ca.json')), key=lambda calicityinfo: calicityinfo['name'])

        self.counties = []
        self.latitudes = []
        self.longitudes = []
        self.cities = []

        for city in myjson:
            if "County" not in city['name']:
                self.cities.append(city['name'])
                self.counties.append(city['county_name'])
                self.latitudes.append(city['primary_latitude'])
                self.longitudes.append(city['primary_longitude'])

    def load_up_selected_data(self, selectedcity):
        """
        If a user selects a different city, loads corresponding data
        into the entries.
        """
        #Clear all entries as a new city has been chosen
        self.longitudeentry.delete(0, 'end')
        self.latitudeentry.delete(0, 'end')
        self.countyentry.delete(0, 'end')

        #Find the index of the new city and load all data into all entries
        cityindex = self.cities.index(selectedcity.get())
        self.longitudeentry.insert(0, self.longitudes[cityindex])
        self.latitudeentry.insert(0, self.latitudes[cityindex])
        self.countyentry.insert(0, self.counties[cityindex] + " County")


if __name__ == '__main__':
    MyGUI()
