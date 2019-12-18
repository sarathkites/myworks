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
public class Referee_Account {

    //5. referee_account -id,rin_no,fname,lname,category_id,district_id,emailid,phoneno,date_of_reg,status
    public int id;
    public String rin_no, fname, lname;
    public int category_id, district_id;
    public String emailid, phoneno, date_of_reg, status;

    public Referee_Account(int id, String rin_no, String fname, String lname, int category_id, int district_id, String emailid, String phoneno, String date_of_reg, String status) {
        this.id = id;
        this.rin_no = rin_no;
        this.fname = fname;
        this.lname = lname;
        this.category_id = category_id;
        this.district_id = district_id;
        this.emailid = emailid;
        this.phoneno = phoneno;
        this.date_of_reg = date_of_reg;
        this.status = status;
    }

    @Override
    public String toString() {
        return "Referee_Account{" + "id=" + id + ", rin_no=" + rin_no + ", fname=" + fname + ", lname=" + lname + ", category_id=" + category_id + ", district_id=" + district_id + ", emailid=" + emailid + ", phoneno=" + phoneno + ", date_of_reg=" + date_of_reg + ", status=" + status + '}';
    }

}
