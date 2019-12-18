package db;

import java.sql.*;

public class DBCon {

    Connection con = null;
    Statement stmt = null;
    static final String Path = "/home/sarath/coding/javaprojects/referee_job_allocation/RefereeServer/out/referee.db";
    
    static final String DBPATH =Path;
    static final String DRIVER = "org.sqlite.JDBC";
    static final String CONSTRING = "jdbc:sqlite:"+DBPATH;
    public static String tables[] =  new String[12];
    public DBCon() {

        try {
            Class.forName(DRIVER);
            con = DriverManager.getConnection(CONSTRING);
            System.out.println("Database Created");
            con.setAutoCommit(false);
            stmt = con.createStatement();
            System.out.println("Statement Created");

        } catch (Exception e) {
            System.out.println("DBConn Constructor Err>>" + e);
        }
    }

    public void createTables() {
        try {

            //1. admin_login - id,uname,passwd,status
            tables[0] = "CREATE TABLE IF NOT EXISTS admin_login("
                    + "id INT,"
                    + "uname VARCHAR(50),"
                    + "passwd VARCHAR(50),"
                    + "status VARCHAR(50))";
                  
            //2. referee_login - id,rin_no,passwd,status
            tables[1] = "CREATE TABLE IF NOT EXISTS referee_login("
                    + "id INT,"
                    + "rin_no VARCHAR(50),"
                    + "passwd VARCHAR(50),"
                    + "status VARCHAR(150))";
            
            //3. state_master - id,state_name,state_short_code       
            tables[2] = "CREATE TABLE IF NOT EXISTS state_master("
                    + "id INT,"
                    + "state_name VARCHAR(100),"
                    + "state_short_code VARCHAR(10))";
            
            //4. district_master - id,district_name,district_short_code,state_id
            tables[3] = "CREATE TABLE IF NOT EXISTS district_master("
                    + "id INT,"
                    + "district_name VARCHAR(100),"
                    + "district_short_code VARCHAR(10),"
                    + "state_id INT)";
            
            //5. referee_account -id,rin_no,fname,lname,category_id,district_id,emailid,phoneno,date_of_reg,status
            tables[4] = "CREATE TABLE IF NOT EXISTS referee_account("
                    + "id INT,"
                    + "rin_no VARCHAR(50),"
                    + "fname VARCHAR(50),"
                    + "lname VARCHAR(50),"
                    + "category_id INT,"
                    + "district_id INT,"
                    + "emailid VARCHAR(250),"
                    + "phoneno VARCHAR(20),"
                    + "date_of_reg VARCHAR(100),"
                    + "status VARCHAR(20))";
            
            //6. tournament_master - id,tournament_name,date_of_tournament,time_of_tournament,venue_name,addr1,addr2,addr3,pincode,status
            tables[5] = "CREATE TABLE IF NOT EXISTS tournament_master("
                    + "id INT,"
                    + "tournament_name VARCHAR(250),"
                    + "date_of_tournament VARCHAR(50),"
                    + "time_of_tournament VARCHAR(50),"
                    + "venue_name VARCHAR(250),"
                    + "addr1 VARCHAR(250),"
                    + "addr2 VARCHAR(250),"
                    + "addr3 VARCHAR(250),"
                    + "pincode VARCHAR(15),"
                    + "status VARCHAR(50))";
            
            //7. tournament_duty - id,tournament_id,referee_id,role_id
            tables[6] = "CREATE TABLE IF NOT EXISTS tournament_duty("
                    + "id INT,"
                    + "tournament_id INT,"
                    + "referee_id INT,"
                    + "role_id INT)";
            
            //8. referee_duty_log - id,tournament_id,referee_id,role_id,dt,tm,status
            tables[7] = "CREATE TABLE IF NOT EXISTS referee_duty_log("
                    + "id INT,"
                    + "tournament_id INT,"
                    + "referee_id INT,"
                    + "role_id INT,"
                    + "dt VARCHAR(25),"
                    + "tm VARCHAR(25),"
                    + "status VARCHAR(20))";
                    
            //9. role_master - id,role_name,role_short_code
            tables[8] = "CREATE TABLE IF NOT EXISTS role_master("
                    + "id INT,"
                    + "role_name VARCHAR(150),"
                    + "role_short_code VARCHAR(10))";
            
            //10. message_template - id,action_type,message
            tables[9] = "CREATE TABLE IF NOT EXISTS message_template("
                    + "id INT,"
                    + "action_type VARCHAR(150),"
                    + "message VARCHAR(1000))";
            
            //11. user_log - id,referee_id,action,dt,tm
            tables[10] = "CREATE TABLE IF NOT EXISTS user_log("
                    + "id INT,"
                    + "referee_id INT,"
                    + "action VARCHAR(1000),"
                    + "dt VARCHAR(50),"
                    + "tm VARCHAR(50))";
            
            //12. category_master - id,category_name,category_descp
            tables[11] = "CREATE TABLE IF NOT EXISTS category_master("
                    + "id INT,"
                    + "category_name VARCHAR(150),"
                    + "category_descp VARCHAR(1000))";
            
            
            for(int i=0;i<tables.length;i++){
                int j = executeUpdate(tables[i]);

                if (j > 0) {
                    System.out.println("Table Created");
                }
            }
            
        } catch (Exception e) {
            System.out.println("DBConn Create Tables Err>>" + e);
        }
    }

    public void dropTables() {
        try {
            
            tables = new String[]{"admin_login","referee_login","state_master",
                        "district_master","referee_account","tournament_master",
                        "tournament_duty","referee_duty_log","role_master",
                        "message_template","user_log","category_master"};
            
            for(int i=0;i<tables.length;i++){
                int j = executeUpdate("DROP TABLE IF EXISTS "+tables[i]);

                if (j > 0) {
                    System.out.println("Table Deleted");
                }
            }
        } catch (Exception e) {
            System.out.println("DBCon Drop Tables Err>>" + e);
        }

    }

    public int executeUpdate(String query) {
        int result = 0;
        try {
            System.out.println("DBCon Query>>" + query);
            result = stmt.executeUpdate(query);
            con.commit();
        } catch (Exception e) {
            System.out.println("DBCon Execute Update Error>>" + e);
        }
        return result;
    }

    public ResultSet executeQuery(String query) {
        ResultSet rset = null;
        try {

            System.out.println("DBCon Query>>" + query);
            con.commit();
            rset = stmt.executeQuery(query);

        } catch (Exception e) {
            System.out.println("DBCon Execute Query Err>>" + e);
        }
        return rset;
    }

    public void close() {
        try {
            con.close();
        } catch (Exception e) {
            System.out.println("DBCon Close Err>>" + e);
        }
    }

    public static void main(String args[]) {
        DBCon dbcon = new DBCon();
        //dbcon.createTables();
        //dbcon.dropTables();
        dbcon.close();
    }
}
