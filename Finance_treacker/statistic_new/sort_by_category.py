def sort_operations_by_categories(lst,category):
    if category is not None:
        lst_category =[]
        for item in lst: 
            for keys in item: 
                if keys == category:
                    if item[category] != 0:
                        lst_category.append(item)                   
        return lst_category       
    else:
        return lst 