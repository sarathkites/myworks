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
public class Referee_Duty_Log {
    //8. referee_duty_log - id,tournament_id,referee_id,role_id,dt,tm,status
    public int id,tournament_id,referee_id,role_id;
    public String dt,tm,status;

    public Referee_Duty_Log(int id, int tournament_id, int referee_id, int role_id, String dt, String tm, String status) {
        this.id = id;
        this.tournament_id = tournament_id;
        this.referee_id = referee_id;
        this.role_id = role_id;
        this.dt = dt;
        this.tm = tm;
        this.status = status;
    }

    @Override
    public String toString() {
        return "Referee_Duty_Log{" + "id=" + id + ", tournament_id=" + tournament_id + ", referee_id=" + referee_id + ", role_id=" + role_id + ", dt=" + dt + ", tm=" + tm + ", status=" + status + '}';
    }
    
    
}
