import sqlite3

conn = sqlite3.connect('C:\\Users\\admin\\PycharmProjects\\pythonProject4\\northwind_small.sqlite3')
c = conn.cursor()

def most_expensive():
    sql = "SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10"
    c.execute(sql)
    c_result = c.fetchall()
    print(c_result)

'''[(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0), (29, 'Thüringer Rostbratwurst', 12, 6, '50 bags x 30 sausgs.', 123.79, 0, 0, 0, 1), (9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97, 29, 0, 0, 1), (20, "Sir Rodney's Marmalade", 8, 3, '30 gift boxes', 81, 40, 0, 0, 0), (18, 'Carnarvon Tigers', 7, 8, '16 kg pkg.', 62.5, 42, 0, 0, 0), (59, 'Raclette Courdavault', 28, 4, '5 kg pkg.', 55, 79, 0, 0, 0), (51, 'Manjimup Dried Apples', 24, 7, '50 - 300 g pkgs.', 53, 20, 0, 10, 0), (62, 'Tarte au sucre', 29, 3, '48 pies', 49.3, 17, 0, 0, 0), (43, 'Ipoh Coffee', 20, 1, '16 - 500 g tins', 46, 17, 10, 25, 0), (28, 'Rössle Sauerkraut', 12, 7, '25 - 825 g cans', 45.6, 26, 0, 0, 1)]
'''
expensive_items = most_expensive()

def hire_age():
    sql = "SELECT AVG(HireDate - BirthDate) FROM Employee"
    c.execute(sql)
    c_result = c.fetchone()
    print(c_result)

'''(37.22222222222222,)
'''
avg_hire_age = hire_age()

def most_expensive_supplier():
    sql = "SELECT * FROM Product INNER JOIN Supplier ON Product.SupplierId = Supplier.Id ORDER BY UnitPrice DESC LIMIT 10"
    c.execute(sql)
    c_result = c.fetchall()
    print(c_result)
'''[(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0, 18, 'Aux joyeux ecclésiastiques', 'Guylène Nodier', 'Sales Manager', '203, Rue des Francs-Bourgeois', 'Paris', 'Western Europe', '75004', 'France', '(1) 03.83.00.68', '(1) 03.83.00.62', None), (29, 'Thüringer Rostbratwurst', 12, 6, '50 bags x 30 sausgs.', 123.79, 0, 0, 0, 1, 12, 'Plutzer Lebensmittelgroßmärkte AG', 'Martin Bein', 'International Marketing Mgr.', 'Bogenallee 51', 'Frankfurt', 'Western Europe', '60439', 'Germany', '(069) 992755', None, 'Plutzer (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/plutzer.htm#'), (9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97, 29, 0, 0, 1, 4, 'Tokyo Traders', 'Yoshi Nagase', 'Marketing Manager', '9-8 Sekimai Musashino-shi', 'Tokyo', 'Eastern Asia', '100', 'Japan', '(03) 3555-5011', None, None), (20, "Sir Rodney's Marmalade", 8, 3, '30 gift boxes', 81, 40, 0, 0, 0, 8, 'Specialty Biscuits, Ltd.', 'Peter Wilson', 'Sales Representative', "29 King's Way", 'Manchester', 'British Isles', 'M14 GSD', 'UK', '(161) 555-4448', None, None), (18, 'Carnarvon Tigers', 7, 8, '16 kg pkg.', 62.5, 42, 0, 0, 0, 7, 'Pavlova, Ltd.', 'Ian Devling', 'Marketing Manager', '74 Rose St. Moonie Ponds', 'Melbourne', 'Victoria', '3058', 'Australia', '(03) 444-2343', '(03) 444-6588', None), (59, 'Raclette Courdavault', 28, 4, '5 kg pkg.', 55, 79, 0, 0, 0, 28, 'Gai pâturage', 'Eliane Noz', 'Sales Representative', 'Bat. B 3, rue des Alpes', 'Annecy', 'Western Europe', '74000', 'France', '38.76.98.06', '38.76.98.58', None), (51, 'Manjimup Dried Apples', 24, 7, '50 - 300 g pkgs.', 53, 20, 0, 10, 0, 24, "G'day, Mate", 'Wendy Mackenzie', 'Sales Representative', "170 Prince Edward Parade Hunter's Hill", 'Sydney', 'NSW', '2042', 'Australia', '(02) 555-5914', '(02) 555-4873', "G'day Mate (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/gdaymate.htm#"), (62, 'Tarte au sucre', 29, 3, '48 pies', 49.3, 17, 0, 0, 0, 29, "Forêts d'érables", 'Chantal Goulet', 'Accounting Manager', '148 rue Chasseur', 'Ste-Hyacinthe', 'North America', 'J2S 7S8', 'Canada', '(514) 555-2955', '(514) 555-2921', None), (43, 'Ipoh Coffee', 20, 1, '16 - 500 g tins', 46, 17, 10, 25, 0, 20, 'Leka Trading', 'Chandra Leka', 'Owner', '471 Serangoon Loop, Suite #402', 'Singapore', 'South-East Asia', '0512', 'Singapore', '555-8787', None, None), (28, 'Rössle Sauerkraut', 12, 7, '25 - 825 g cans', 45.6, 26, 0, 0, 1, 12, 'Plutzer Lebensmittelgroßmärkte AG', 'Martin Bein', 'International Marketing Mgr.', 'Bogenallee 51', 'Frankfurt', 'Western Europe', '60439', 'Germany', '(069) 992755', None, 'Plutzer (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/plutzer.htm#')]
'''
ten_most_expensive = most_expensive_supplier()

def largest_category():
    sql = "SELECT MAX(CategoryName) FROM Category INNER JOIN Product on Category.Id = Product.CategoryId"
    c.execute(sql)
    c_result = c.fetchone()
    print(c_result)

'''('Seafood',)'''
largest_category = largest_category()