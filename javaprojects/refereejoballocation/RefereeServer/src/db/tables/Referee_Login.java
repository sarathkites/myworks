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
public class Referee_Login {
    //2. referee_login - id,rin_no,passwd,status
    
    public int id;
    public String rin_no,passwd,status;

    public Referee_Login(int id, String rin_no, String passwd, String status) {
        this.id = id;
        this.rin_no = rin_no;
        this.passwd = passwd;
        this.status = status;
    }

    @Override
    public String toString() {
        return "Referee_Login{" + "id=" + id + ", rin_no=" + rin_no + ", passwd=" + passwd + ", status=" + status + '}';
    }
    
    
}
