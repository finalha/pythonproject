__author__ = '16101210-15'
dbnames = ['NSDEV10213','NSTEST10057','NSTEST10057','NSTEST10057','NSTEST10057']
for dbname in dbnames:
    print("DROP LOGIN ["+dbname+"];\r\n")
    print("EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = N'"+dbname+"';\r\n")
    print("DROP DATABASE ["+dbname+"];\r\n")