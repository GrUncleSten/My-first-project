def sort_operations_by_categories(lst,category):
    lst_category =[]
    for item in lst:  
        if item["category"] == category:
            lst_category.append(item)
    return lst_category        