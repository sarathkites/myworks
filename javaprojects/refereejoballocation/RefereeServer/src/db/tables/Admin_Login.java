/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package db.tables;

/**
 *
 * @author sarath
 */
public class Admin_Login {
    //1. admin_login - id,uname,passwd,status
    
    public int id;
    public String uname,passwd,status;

    public Admin_Login(int id, String uname, String passwd, String status) {
        this.id = id;
        this.uname = uname;
        this.passwd = passwd;
        this.status = status;
    }

    @Override
    public String toString() {
        return "Admin_Login{" + "id=" + id + ", uname=" + uname + ", passwd=" + passwd + ", status=" + status + '}';
    }
    
    
}
