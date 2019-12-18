/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package db;


import java.sql.ResultSet;
import java.util.ArrayList;

import db.tables.Admin_Login;
import db.tables.District_Master;
import db.tables.Referee_Login;
import db.tables.State_Master;

/**
 *
 * @author root
 */
public class DBProcess extends DBCon{
 
    //1. admin_login - id,uname,passwd,status
    /******************************************************************/
    public int getMaxID_admin_login(){
        int mid =0;
        try {
            String query="SELECT MAX(id) FROM admin_login";
             ResultSet rset = executeQuery(query);
            if(rset.next()){
                mid = rset.getInt(1);
            }
        } catch (Exception e) {
            System.out.println("getMaxID_admin_login Err>>"+e);
        }
        return mid;
    }

    public int insert_admin_login(Admin_Login obj){
        int result =0;
        try {
            String query="INSERT INTO admin_login(id,uname,passwd,status) VALUES(id,'"+obj.uname+"','"+obj.passwd+"','"+obj.status+"')";
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("insert_admin_login Err>>"+e);
        }
        return result;
    }
    public int delete_admin_login(int id){
        int result = 0;
        try {
            String query="DELETE FROM admin_login WHERE id="+id;
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("delete_admin_login Err>>"+e);
        }
        return result;
    }
    
    public int update_admin_login(Admin_Login obj){
        int result =0;
        try {
            String query="UPDATE admin_login SET uname='"+obj.uname+"',passwd='"+obj.passwd+"',status='"+obj.status+"' WHERE id="+obj.id;
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("update_admin_login Err>>"+e);
        }
        return result;
    }
     public Admin_Login select_admin_login(int id){
        Admin_Login obj =null;
        try {
            String query="SELECT id,uname,passwd,status FROM admin_login WHERE id="+id;
            ResultSet rset = executeQuery(query);
            if(rset.next()){
               id = rset.getInt("id");
               String uname = rset.getString("uname");
               String passwd = rset.getString("passwd");
               String status = rset.getString("status");
               
               obj = new Admin_Login(id, uname, passwd, status);
            }
        } catch (Exception e) {
            System.out.println("select_admin_login Err>>"+e);
        }
        return obj;
    }

    public ArrayList<Admin_Login> selectAll_admin_login(){
        ArrayList<Admin_Login> objList = new ArrayList<Admin_Login>();
        try {
            String query="SELECT id,uname,passwd,status FROM admin_login ";
            ResultSet rset = executeQuery(query);
            while(rset.next()){
               Admin_Login obj;
               int id = rset.getInt("id");
               String uname = rset.getString("uname");
               String passwd = rset.getString("passwd");
               String status = rset.getString("status");
               
               obj = new Admin_Login(id, uname, passwd, status);
               objList.add(obj);
               
            }
        } catch (Exception e) {
            System.out.println("selectAll_admin_login Err>>"+e);
        }
        return objList;
    }
   
    
    /******************************************************************/
   
    
    //2. referee_login - id,rin_no,passwd,status
    /******************************************************************/
    public int getMaxID_referee_login(){
        int mid =0;
        try {
            String query="SELECT MAX(id) FROM referee_login";
             ResultSet rset = executeQuery(query);
            if(rset.next()){
                mid = rset.getInt(1);
            }
        } catch (Exception e) {
            System.out.println("getMaxID_referee_login Err>>"+e);
        }
        return mid;
    }

    public int insert_referee_login(Referee_Login obj){
        int result =0;
        try {
            String query="INSERT INTO referee_login(id,rin_no,passwd,status) VALUES("+obj.id+",'"+obj.rin_no+"','"+obj.passwd+"','"+obj.status+"')";
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("insert_referee_login Err>>"+e);
        }
        return result;
    }
    public int delete_referee_login(int id){
        int result = 0;
        try {
            String query="DELETE FROM referee_login WHERE id="+id;
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("delete_referee_login Err>>"+e);
        }
        return result;
    }
    
    public int update_referee_login(Referee_Login obj){
        int result =0;
        try {
            String query="UPDATE referee_login SET rin_no='"+obj.rin_no+"',passwd='"+obj.passwd+"',status='"+obj.status+"' WHERE id="+obj.id;
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("update_referee_login Err>>"+e);
        }
        return result;
    }
     public Referee_Login select_referee_login(int id){
        Referee_Login obj =null;
        try {
            String query="SELECT id,rin_no,passwd,status FROM referee_login WHERE id="+id;
            ResultSet rset = executeQuery(query);
            if(rset.next()){
               id = rset.getInt("id");
               String rin_no = rset.getString("rin_no");
               String passwd = rset.getString("passwd");
               String status = rset.getString("status");
               
               obj = new Referee_Login(id, rin_no, passwd, status);
            }
        } catch (Exception e) {
            System.out.println("select_referee_login Err>>"+e);
        }
        return obj;
    }

    public ArrayList<Referee_Login> selectAll_referee_login(){
        ArrayList<Referee_Login> objList = new ArrayList<Referee_Login>();
        try {
            String query="SELECT id,rin_no,passwd,status FROM referee_login ";
            ResultSet rset = executeQuery(query);
            while(rset.next()){
               Referee_Login obj;
               int id = rset.getInt("id");
               String rin_no = rset.getString("rin_no");
               String passwd = rset.getString("passwd");
               String status = rset.getString("status");
               
               obj = new Referee_Login(id, rin_no, passwd, status);
               objList.add(obj);
            }
        } catch (Exception e) {
            System.out.println("selectAll_referee_login Err>>"+e);
        }
        return objList;
    }
   
    
    /******************************************************************/
    //3. state_master - id,state_name,state_short_code
    /******************************************************************/
    public int getMaxID_state_master(){
        int mid =0;
        try {
            String query="SELECT MAX(id) FROM state_master";
             ResultSet rset = executeQuery(query);
            if(rset.next()){
                mid = rset.getInt(1);
            }
        } catch (Exception e) {
            System.out.println("getMaxID_state_master Err>>"+e);
        }
        return mid;
    }

    public int insert_state_master(State_Master obj){
        int result =0;
        try {
            String query="INSERT INTO state_master(id,state_name,state_short_code) VALUES("+obj.id+",'"+obj.state_name+"','"+obj.state_short_code+"')";
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("insert_state_master Err>>"+e);
        }
        return result;
    }
    public int delete_state_master(int id){
        int result = 0;
        try {
            String query="DELETE FROM state_master WHERE id="+id;
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("delete_state_master Err>>"+e);
        }
        return result;
    }
    
    public int update_state_master(State_Master obj){
        int result =0;
        try {
            String query="UPDATE state_master SET state_name='"+obj.state_name+"',state_short_code='"+obj.state_short_code+"' WHERE id="+obj.id;
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("update_state_master Err>>"+e);
        }
        return result;
    }
     public State_Master select_state_master(int id){
        State_Master obj =null;
        try {
            String query="SELECT id,state_name,state_short_code FROM state_master WHERE id="+id;
            ResultSet rset = executeQuery(query);
            if(rset.next()){
                //id,state_name,state_short_code
               id = rset.getInt("id");
               String state_name = rset.getString("state_name");
               String state_short_code = rset.getString("state_short_code");
               
               obj = new State_Master(id, state_name, state_short_code);
               
            }
        } catch (Exception e) {
            System.out.println("select_state_master Err>>"+e);
        }
        return obj;
    }

    public ArrayList<State_Master> selectAll_state_master(){
        ArrayList<State_Master> objList = new ArrayList<State_Master>();
        try {
            String query="SELECT ** FROM state_master ";
            ResultSet rset = executeQuery(query);
            while(rset.next()){
               State_Master obj;
               int id = rset.getInt("id");
               String state_name = rset.getString("state_name");
               String state_short_code = rset.getString("state_short_code");
               
               obj = new State_Master(id, state_name, state_short_code);
               objList.add(obj);
            }
        } catch (Exception e) {
            System.out.println("selectAll_state_master Err>>"+e);
        }
        return objList;
    }
   
    
    /******************************************************************/
    
    //4. district_master - id,district_name,district_short_code,state_id
    /******************************************************************/
    public int getMaxID_district_master(){
        int mid =0;
        try {
            String query="SELECT MAX(id) FROM district_master";
             ResultSet rset = executeQuery(query);
            if(rset.next()){
                mid = rset.getInt(1);
            }
        } catch (Exception e) {
            System.out.println("getMaxID_district_master Err>>"+e);
        }
        return mid;
    }

    public int insert_district_master(District_Master obj){
        int result =0;
        try {
            String query="INSERT INTO district_master(id,district_name,district_short_code,state_id) VALUES("+obj.id+",'"+obj.district_name+"','"+obj.district_short_code+"',"+obj.state_id+")";
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("insert_district_master Err>>"+e);
        }
        return result;
    }
    public int delete_district_master(int id){
        int result = 0;
        try {
            String query="DELETE FROM district_master WHERE id="+id;
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("delete_district_master Err>>"+e);
        }
        return result;
    }
    
    public int update_district_master(District_Master obj){
        int result =0;
        try {
            String query="UPDATE district_master SET district_name='"+obj.district_name+"',district_short_code='"+obj.district_short_code+"',state_id="+obj.state_id+" WHERE id="+obj.id;
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println("update_district_master Err>>"+e);
        }
        return result;
    }
     public District_Master select_district_master(int id){
        District_Master obj =null;
        try {
            String query="SELECT ** FROM district_master WHERE id="+id;
            ResultSet rset = executeQuery(query);
            if(rset.next()){
                //id,district_name,district_short_code,state_id
                id = rset.getInt("id");
                String district_name = rset.getString("district_name");
                String district_short_code = rset.getString("district_short_code");
                int state_id = rset.getInt("state_id");
                
                obj = new District_Master(id, district_name, district_short_code, state_id);
                
            }
        } catch (Exception e) {
            System.out.println("select_district_master Err>>"+e);
        }
        return obj;
    }

    public ArrayList<District_Master> selectAll_district_master(){
        ArrayList<District_Master> objList = new ArrayList<District_Master>();
        try {
            String query="SELECT ** FROM district_master ";
            ResultSet rset = executeQuery(query);
            while(rset.next()){
               District_Master obj;
               int id = rset.getInt("id");
                String district_name = rset.getString("district_name");
                String district_short_code = rset.getString("district_short_code");
                int state_id = rset.getInt("state_id");
                
                obj = new District_Master(id, district_name, district_short_code, state_id);
                objList.add(obj);
            }
        } catch (Exception e) {
            System.out.println("selectAll_district_master Err>>"+e);
        }
        return objList;
    }
   
    
    /******************************************************************/
    //5. referee_account -id,rin_no,fname,lname,category_id,district_id,emailid,phoneno,date_of_reg,status
    //6. tournament_master - id,tournament_name,date_of_tournament,time_of_tournament,venue_name,addr1,addr2,addr3,pincode,status
    //7. tournament_duty - id,tournament_id,referee_id,role_id
    //8. referee_duty_log - id,tournament_id,referee_id,role_id,dt,tm,status
    //9. role_master - id,role_name,role_short_code
    //10. message_template - id,action_type,message
    //11. user_log - id,referee_id,action,dt,tm
    //12. category_master - id,category_name,category_descp
    
    /******************************************************************
    public int getMaxID_(){
        int mid =0;
        try {
            String query="SELECT MAX(id) FROM **";
             ResultSet rset = executeQuery(query);
            if(rset.next()){
                mid = rset.getInt(1);
            }
        } catch (Exception e) {
            System.out.println(" Err>>"+e);
        }
        return mid;
    }

    public int insert_(Object obj){
        int result =0;
        try {
            String query="INSERT INTO **() VALUES()";
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println(" Err>>"+e);
        }
        return result;
    }
    public int delete_(int id){
        int result = 0;
        try {
            String query="DELETE FROM ** WHERE id="+id;
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println(" Err>>"+e);
        }
        return result;
    }
    
    public int update_(Object obj){
        int result =0;
        try {
            String query="UPDATE ** SET ** WHERE id="+obj.id;
             result = executeUpdate(query);
        } catch (Exception e) {
            System.out.println(" Err>>"+e);
        }
        return result;
    }
     public Object select_(int id){
        Object obj =null;
        try {
            String query="SELECT ** FROM ** WHERE id="+id;
            ResultSet rset = executeQuery(query);
            if(rset.next()){
               int id = rset.getInt("id");
               String uname = rset.getString("uname");
               
            }
        } catch (Exception e) {
            System.out.println(" Err>>"+e);
        }
        return obj;
    }

    public ArrayList<Object> selectAll_(){
        ArrayList<Object> objList = new ArrayList<Object>();
        try {
            String query="SELECT ** FROM ** ";
            ResultSet rset = executeQuery(query);
            while(rset.next()){
               
            }
        } catch (Exception e) {
            System.out.println(" Err>>"+e);
        }
        return objList;
    }
   
    
    /******************************************************************/
   
}
