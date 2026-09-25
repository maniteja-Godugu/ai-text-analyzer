from app.db_connection import get_connection

def insert_data(prompt,summary,sentiment,difficulty):
    conn=get_connection()
    cursor=conn.cursor()
    data=(prompt,summary,sentiment,difficulty)
    insert_query='''INSERT INTO analyze(Prompt,Summary,Sentimenti,Difficulty)
    values(?,?,?,?)
    '''
    cursor.execute(insert_query,data)
    conn.commit()
    conn.close()

def get_history():
    conn=get_connection()
    cursor=conn.cursor()
    get_history_query='''SELECT Id,Prompt,Summary FROM analyze'''
    cursor.execute(get_history_query)
    result=cursor.fetchall()
    conn.close()
    if result:
        return result
    
    return None

    
    
    
    
def get_history_by_id(id):
    conn=get_connection()
    cursor=conn.cursor()
    get_history_query='''SELECT Id,Prompt,Summary FROM analyze WHERE Id=?'''
    cursor.execute(get_history_query,(id,))
    result=cursor.fetchone() 
    conn.close()
    if result:
        return dict(result)
    return None
    
def delete_history_by_id(id):
    conn=get_connection()
    cursor=conn.cursor()
    delete_query='''DELETE FROM analyze WHERE Id=?'''
    cursor.execute(delete_query,(id,))
    conn.commit()
    conn.close()