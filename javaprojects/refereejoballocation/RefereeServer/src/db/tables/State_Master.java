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
public class State_Master {
    //3. state_master - id,state_name,state_short_code
    public int id;
    public String state_name,state_short_code;

    public State_Master(int id, String state_name, String state_short_code) {
        this.id = id;
        this.state_name = state_name;
        this.state_short_code = state_short_code;
    }

    @Override
    public String toString() {
        return "State_Master{" + "id=" + id + ", state_name=" + state_name + ", state_short_code=" + state_short_code + '}';
    }
    
    
}
