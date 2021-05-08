# install chrome web driver(version of driver must be same as the version of chrome browser) in same folder or 
# add path of chrome driver in this code
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import pandas as pd
# add your chrome driver path in ---->executable_path = "your path" 
driver = webdriver.Chrome(executable_path="C:\\Users\\devsa\\Downloads\\Programs\\chromedriver.exe")
url="https://www.amazon.in/"
# driver.get(url)

header_length = 0
header_string = ''
count = 0
description = ''
brand_name_list = []
key_list =[]
list_of_dict = []


def csv_file(lst):
    csv_columns = ['brand_name', 'article_name', 'gender', 'fitting_type', 'Label_Size', 'Standard_Size',
     'Waist', 'Inseam_length', 'Leg_opening','Hip']
    try:
        with open('file_name_1.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in lst:
                writer.writerow(data)
    except IOError:     
        print("I/O error")
    
    # with open('file_name.csv', 'w') as csvfile: 
    #     writer = csv.DictWriter(csvfile, fieldnames = csv_columns) 
    #     writer.writeheader() 
    #     writer.writerows(lst)

def data_prettify(file_name):
    df = pd.read_csv(file_name)
    df1 = df.iloc[:,0:6]
    lst1 = df.columns

    for j in range(6,len(lst1)):
        print(df.iloc[:,j])
            
        lst = list(df.iloc[:,j])
        for i in range(len(lst)):
            try:
                if 'ches' in lst[i]:
                    temp_item =lst[i].split(" ")
                    lst[i] = temp_item[0]
        

            except TypeError:
                pass
                    
        
        df1[f"{lst1[j]}"] = lst
        print(df1)
    df1["unit"] = "inches"
    df1.to_csv(f'{file_name}',index =False)

def index_containing_substring(the_list,entity,optional_entity):
    for i, s in enumerate(the_list):
        if entity in s:
              return i
        elif optional_entity in s:
            return i


def file_header():
    soup = BeautifulSoup(driver.page_source,'html.parser')
    header_elements = soup.find_all('th')
    header_elements_lst0 = ['brand_name','article_name','gender','fitting_type']
    # header_elements_lst0.insert(0,'brand_name ')
    # header_elements_lst0.insert(1,'article_name ')
    # header_elements_lst0.insert(2,"gender")
    # header_elements_lst0.insert(3,"fitting_type") 
    header_elements_lst1= [] 


    for y in header_elements:
        lst_item = y.get_text()
        lst_item =lst_item.strip('\n')
        lst_item= lst_item.replace('\n\n\n',' ')

        header_elements_lst1.append(lst_item)
   
        
    for i in header_elements_lst1:
            header_elements_lst0.append(i)
    print(header_elements_lst0)
    # This code is to get the file name 
    length_of_header = len(header_elements)
    # print(length_of_header)
    global header_length
    header_length = length_of_header 
    global header_string
    # header_string = listToString(header_elements_lst0)
    print(header_string)

    return header_elements_lst0


def size_chart_record(fitting_type_str):

    soup = BeautifulSoup(driver.page_source,'html.parser')
    size_row = soup.find_all('span',{'class': 'a-nowrap'})
    data_list = []
    global  list_of_dict 
    for i in size_row:
        # print(i.get_text())
        data_list.append(i.get_text())
    # print(data_list)
    
    length_of_data_list = len(data_list)
    try:
        no_matrix_row = int(len(data_list)/header_length) 
    except (AttributeError,ZeroDivisionError):
        print('no such attribute')

    try:
        arr = np.array(data_list).reshape(no_matrix_row,header_length)
        # print(arr)
        
        header_list = file_header()
        print(header_list)
        brand_index=index_containing_substring(header_list,'brand','@')
        article_name_index=index_containing_substring(header_list,'article_name','@')
        gender_index=index_containing_substring(header_list,'gender','@')
        fitting_type_index=index_containing_substring(header_list,'fitting','@')
        lable_size_index=index_containing_substring(header_list,'Label','@')
        standard_size_index =index_containing_substring(header_list,'Standard','India')
        waist_index=index_containing_substring(header_list,'Waist','@')
        hip_size_index=index_containing_substring(header_list,'Hip','@')
        length_index =index_containing_substring(header_list,'Inseam','length')
        leg_opening_index =index_containing_substring(header_list,'opening','Rise')
        
        
        

    
        csv_list = []
        
        for i in range(len(arr)):
    
            temp_dict = {
                "brand_name":"",
                "article_name":"",
                "gender":"",
                "fitting_type":"",
                "Label_Size":"",
                "Standard_Size":"",
                "Waist":"",
                "Inseam_length":"",
                "Leg_opening":"",
                "Hip":""
               
                }

            csv_list = []
            csv_list.append(description)
            csv_list.insert(1,'Trouser')
            csv_list.insert(2,'male')
            csv_list.insert(3,fitting_type_str)
            # print(description)
            
            list_inside_arr = arr[i]
            # print(list_inside_arr)
            for p in range(len(list_inside_arr)):
                temp = list_inside_arr[p]
                # print(temp)
                csv_list.append(temp)
            # print(csv_list)
            # print("check")
            check_lst = csv_list
            
            # print(check_lst)
            # print(brand_index)
            # print(article_name_index)
            # print(gender_index)
            # print(fitting_type_index)
            # print(lable_size_index)
            # print(standard_size_index)
            # print(shoulder_index)
            # print(chest_index)
            # print(front_index)
            # print(waist_index)
            # print(neck_index)
            # print(sleeve_index)

            try:
                temp_dict["brand_name"]= check_lst[brand_index] 
            except TypeError:
                pass
                # print("type_error")
            try:
                temp_dict["article_name"]= check_lst[article_name_index] 
            except TypeError:
                pass
                # print("type_error")
            try:
                temp_dict["gender"]= check_lst[gender_index] 
            except TypeError:
                # print("type_error")
                pass
            try:
                temp_dict["fitting_type"]= check_lst[fitting_type_index] 
            except TypeError:
                # print("type_error")
                pass
            try:
                temp_dict["Label_Size"]= check_lst[lable_size_index] 
            except TypeError:
                # print("type_error")
                pass
            try:

                temp_dict["Standard_Size"]= check_lst[standard_size_index]
            except TypeError:
                # print("type_error")
                pass 
            try:
                temp_dict["Waist"]= check_lst[waist_index]
            except TypeError:
                # print("type_error")
                pass
            try:
                temp_dict["Inseam_length"]= check_lst[length_index]
            except TypeError:
                # print("type_error")
                pass
            try:
                temp_dict["Leg_opening"]= check_lst[leg_opening_index] 
            except TypeError:
                # print("type_error")
                pass              
            
            try:
                temp_dict["Hip"]= check_lst[hip_size_index]
            except TypeError:
                # print("type_error")
                pass
            
            
            list_of_dict.append(temp_dict)

                # csv_writer.writerow(csv_list)
    except (ValueError,UnboundLocalError):
        print('no such value')

  
    
  
    

    

def fit_type():
    soup = BeautifulSoup(driver.page_source,'html.parser')
    info_list = soup.find('ul',{'class': 'a-unordered-list a-vertical a-spacing-mini'}).findAll('span',recurcive= False)
    # fitting_type0 = info_list[0]
    # fitting_type1 = info_list[1]
    a_dict = {}
    for i in range(len(info_list)):
        a_dict['fitting_tpye_txt%s'%i] = info_list[i].get_text().strip()


        result_temp =  'Fit Type: '
        # print(a_dict['fitting_tpye_txt%s'%i][0:11])
        if a_dict['fitting_tpye_txt%s'%i][0:10] == result_temp:
        # print(fitting_type_txt)
            temp= a_dict['fitting_tpye_txt%s'%i][10:]
            temp=temp.strip("\n\n")
            # print(temp)

            return temp

 




   


def get_url(search_term):
    search_term = search_term.replace(' ', "+")
    tamplet = f"https://www.amazon.in/s?k={search_term}&ref=nb_sb_ss_ts-do-p_1_14"
    return tamplet
# url = get_url(" mens shirts") 
# driver.get(url)
# soup = BeautifulSoup(driver.page_source,'html.parser')
# product_brand= soup.find_all('span', {'class' : 'a-size-base-plus a-color-base'})
# for key_item in product_brand:
#     key = key_item.get_text()
#     key_list.append(key)
# print(key_list)
    

def size_chart_link(key):
    search_key = key +" mens trousers"
    url = get_url(search_key)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    results= soup.find_all('a' , {'class' : 'a-link-normal a-text-normal'})
    product_brand= soup.find_all('span', {'class' : 'a-size-base-plus a-color-base'})
    # disp_list= []
    fit_type_lst = []


    

    for i in range(20):
        item = results[i]
        try:
            brand_name = product_brand[i]
            # print(item)
            global description
            description = str(brand_name.get_text())
            product_name = [[description]]
            
            
            url="https://www.amazon.in" + item.get('href')
            # print(url)
            driver.get(url)
            soup = BeautifulSoup(driver.page_source,'html.parser')
            size_chart_result = soup.find_all('a',{'data-header':'Size Chart'})
            if len(size_chart_result)>0:

                item2=size_chart_result[0] 
                
                

                url = "https://www.amazon.in" + item2.get('href') 
                print(i)
                fitting_type_str=fit_type()
                fit_type_lst.append(fitting_type_str)
                
                driver.get(url)
                file_header()
            

                size_chart_record(fitting_type_str)
        except IndexError:
            # print("index error")
            pass   
            
        
    print(fit_type_lst)


if __name__ =="__main__":
    url = get_url(" mens trousers") 
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    product_brand= soup.find_all('span', {'class' : 'a-size-base-plus a-color-base'})
    # void_list = ["AD & AV","JACK"]
    try:
        for i in range(7):
            for key_item in product_brand:
                key = key_item.get_text()
                # if key not in void_list:
                key_list.append(key)
            next_page_link = []
            soup = BeautifulSoup(driver.page_source,'html.parser')
            next_page_link= soup.find("li",{"class":"a-last"}).findAll('a',recurcive= False)
            try:
                next_page_item = next_page_link[0]  
                url="https://www.amazon.in" + next_page_item.get('href')
                driver.get(url)   
            except IndexError:
                # print("index error") 
                pass
            
        print(key_list) 
        # set_keys=set(key_list)
        # key_list = list(set_keys) 
        # print(key_list) 
    except IndexError:
        print("index error")    
        
        
    for i in range(len(key_list)-1):
    # for i in range(10):
            size_chart_link(key_list[i])
        



    csv_file(list_of_dict)

    data_prettify('file_name_1.csv')