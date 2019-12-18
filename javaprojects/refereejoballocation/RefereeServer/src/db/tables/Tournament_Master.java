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
public class Tournament_Master {
    //6. tournament_master - id,tournament_name,date_of_tournament,time_of_tournament,venue_name,addr1,addr2,addr3,pincode,status
    
    public int id;
    public String tournament_name,date_of_tournament,time_of_tournament,venue_name,addr1,addr2,addr3,pincode,status;

    public Tournament_Master(int id, String tournament_name, String date_of_tournament, String time_of_tournament, String venue_name, String addr1, String addr2, String addr3, String pincode, String status) {
        this.id = id;
        this.tournament_name = tournament_name;
        this.date_of_tournament = date_of_tournament;
        this.time_of_tournament = time_of_tournament;
        this.venue_name = venue_name;
        this.addr1 = addr1;
        this.addr2 = addr2;
        this.addr3 = addr3;
        this.pincode = pincode;
        this.status = status;
    }

    @Override
    public String toString() {
        return "Tournament_Master{" + "id=" + id + ", tournament_name=" + tournament_name + ", date_of_tournament=" + date_of_tournament + ", time_of_tournament=" + time_of_tournament + ", venue_name=" + venue_name + ", addr1=" + addr1 + ", addr2=" + addr2 + ", addr3=" + addr3 + ", pincode=" + pincode + ", status=" + status + '}';
    }
    
    
}
