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
public class Role_Master {
    //9. role_master - id,role_name,role_short_code
    public int id;
    public String role_name,role_short_code;

    public Role_Master(int id, String role_name, String role_short_code) {
        this.id = id;
        this.role_name = role_name;
        this.role_short_code = role_short_code;
    }

    @Override
    public String toString() {
        return "Role_Master{" + "id=" + id + ", role_name=" + role_name + ", role_short_code=" + role_short_code + '}';
    }
    
    
}
