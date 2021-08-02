import pyodbc 
import json
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
class sad():

  def __init__(self):
    self.server = '127.0.0.1' 
    self.database = 'mydb' 
    self.username = 'sa' 
    self.password = '1123' 

  def go(self,id):  
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
    cursor = cnxn.cursor()
    #Sample select query
    cursor.execute(f"""select 
      sickbed.[病床代碼],
      sickbed.[病房代碼]
    from 
      [dbo].[病人] patient
      join [dbo].[醫生] doctor on doctor.醫生代碼 = patient.醫生代碼
      join [dbo].[病房] sickroom on sickroom.科別代碼 =doctor.科別代碼
      join [dbo].[病床] sickbed on sickbed.病房代碼 = sickroom.病房代碼
    where patient.病歷代碼 = {id} """) 
    row = cursor.fetchone() 
    data=[]
    ids=1
    nodata=sad().go1(id)
    while row: 
      if nodata==[]:
        data.append({'id':ids,'Ward_code':row[1],'Bed_code':row[0]})
        ids+=1
      else:
        for nodatas in nodata:
          if nodatas!={'Ward_code':row[1],'Bed_code':row[0]} : 
            data.append({'id':ids,'Ward_code':row[1],'Bed_code':row[0]})
            ids+=1    
      row = cursor.fetchone()  
    str1 = json.dumps(data)
    return str1

  def go1(self,id):
      cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
      cursor = cnxn.cursor()
      #Sample select query
      cursor.execute(f"""select S.病房代碼,S.病床代碼  from [dbo].住院 s
                          join [dbo].病人 a on a.病歷代碼=s.病歷代碼
                            
                          where s.病歷代碼={id} and s.離院日期 is NULL""") 
      row = cursor.fetchone() 
      data=[]
      while row: 
          data.append({'Ward_code':row[0],'Bed_code':row[1]})
          row = cursor.fetchone()
      print(data)
      return data

s=sad().go('63599392')
print(s)
s=sad().go1('63599392')
for s in s:
  print(s)    
