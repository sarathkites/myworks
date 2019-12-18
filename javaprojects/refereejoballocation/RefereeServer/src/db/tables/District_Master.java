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
public class District_Master {
    //4. district_master - id,district_name,district_short_code,state_id
    public int id;
    public String district_name,district_short_code;
    public int state_id;

    public District_Master(int id, String district_name, String district_short_code, int state_id) {
        this.id = id;
        this.district_name = district_name;
        this.district_short_code = district_short_code;
        this.state_id = state_id;
    }

    @Override
    public String toString() {
        return "District_Master{" + "id=" + id + ", district_name=" + district_name + ", district_short_code=" + district_short_code + ", state_id=" + state_id + '}';
    }
    
    
}
