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
public class Tournament_Duty {
    //7. tournament_duty - id,tournament_id,referee_id,role_id
    public int id,tournament_id,referee_id,role_id;

    public Tournament_Duty(int id, int tournament_id, int referee_id, int role_id) {
        this.id = id;
        this.tournament_id = tournament_id;
        this.referee_id = referee_id;
        this.role_id = role_id;
    }

    @Override
    public String toString() {
        return "Tournament_Duty{" + "id=" + id + ", tournament_id=" + tournament_id + ", referee_id=" + referee_id + ", role_id=" + role_id + '}';
    }
    
    
}
