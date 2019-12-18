/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package util;

import java.text.SimpleDateFormat;
import java.util.*;
/**
 *
 * @author sarath
 */
public class DateTime {
    public static String getDate(){
        Date curDate = new Date();
        SimpleDateFormat format = new SimpleDateFormat("yyyy/MM/dd");
        String dateToStr = format.format(curDate);
        System.out.println(dateToStr);
        return dateToStr;
    }
    public static String getTime(){
        Date curDate = new Date();
        SimpleDateFormat format = new SimpleDateFormat("hh:mm:ss");
        String timeToStr = format.format(curDate);
        System.out.println(timeToStr);
        return timeToStr;
    }
    public static void main(String[] args) {
        getDate();
        getTime();
    }
}
