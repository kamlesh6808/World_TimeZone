#!/usr/bin/python3

import argparse
import json
import requests
import sys


class Timezone:
    def __init__(self):
        pass

    def parse_arguments(self):
        parser = argparse.ArgumentParser(
            description="World Time Zone Provider.")
        parser.add_argument('--match',
            help="list timezone information from timezone value")
        parser.add_argument('--offset', type=float,
            help="list timezone information from timezone offset")
        return parser.parse_args()

    def timezone_formatter(func):
        def inner_func_of_decor(self,*args) :
            print("--------------------------------------------------------"
                  "--------------------------------------------------------"
                  "------------------")  
            print("SR NO ||       VALUE      ||       ABBR      ||    "
                  "OFFSET     ||     ISDST      ||       TEXT        ||    "
                  "            UTC     ") 
            print("--------------------------------------------------------"
                  "--------------------------------------------------------"
                  "------------------")  
            func(self,*args)
            print("\n------------------------------------------------------"
                  "--------------------------------------------------------"
                  "----------------------")  
        return inner_func_of_decor

    def grab_timezone_information(self):
        try:
            response = requests.get(
                'https://raw.githubusercontent.com/dmfilipenko\
                        /timezones.json/master/timezones.json')
            timezone_content = json.loads(response.text)
            return timezone_content
        except requests.exceptions.ConnectionError as e:
            print("Connection does not established to URL.Check Connectivity."
                  " Error: %(error)s" %{'error': e})
            sys.exit("Exiting Program.")

    @timezone_formatter
    def show_all_timezone_detail(self):
        timezone_content = self.grab_timezone_information()
        sr_number = 1
        for each_timezone in timezone_content:
            print(sr_number, end="     ||  ")
            for key, values in each_timezone.items():
                print(values, end="    || ")
            sr_number+=1
            print("\n\n\n")

    @timezone_formatter
    def matching_value_timezone_detail(self, tz_value_input):
        timezone_content = self.grab_timezone_information()
        timezone_value = [timezone['value'] for timezone in timezone_content]
        sr_number = 1
        if (tz_value_input in timezone_value):
            for timezone in timezone_content:
                if (timezone['value'] == tz_value_input) :
                    print(sr_number, end= "     || ")
                    for key, values in timezone.items():
                        print(values, end = "    || ")
                    sr_number+=1
                    print("\n\n")
        else:
            print("Value does not exist. See information of all timezones to "
                  "verify. Retry post confirmation.")

    @timezone_formatter
    def matching_offset_timezone_detail(self, offset_input):
        timezone_content = self.grab_timezone_information()
        timezone_offset = [timezone['offset'] for timezone in timezone_content]
        sr_number = 1
        if (offset_input in timezone_offset):
            for timezone in timezone_content:
                if (abs(timezone['offset']) == offset_input) :
                    print(sr_number, end="    || ")
                    for key, values in timezone.items():
                        print(values, end="   || ")
                    sr_number+=1
                    print("\n\n")
        else:
            print("Offset does not exist. See information of all timezones to "
                  "verify. Retry post confirmation.")

def main():
    obj_timezone = Timezone()
    args = obj_timezone.parse_arguments()
    if args.match:
        obj_timezone.matching_value_timezone_detail(args.match)
    elif args.offset:
        obj_timezone.matching_offset_timezone_detail(args.offset)
    else:
        if not (args.match or args.offset): 
            obj_timezone.show_all_timezone_detail()

if __name__ == "__main__":
    main()
