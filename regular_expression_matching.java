public class Solution {
    public boolean isMatch(String s, String p) { //base case
        if(p.length() == 0){
            return s.length() == 0;
        }
         
        //special case
        if(p.length() == 1){
             
            //if the length of s is 0, return false
            if(s.length() < 1){
                return false;
            }
             
            /*if the first char of s and the first char of p is not the same, 
            and the char of p is not '.', return false */
            else if((p.charAt(0) != s.charAt(0)) && (p.charAt(0) != '.')){
                return false;
            }
             
            //otherwise, compare the rest of the string of s and p.
            else{
                return isMatch(s.substring(1), p.substring(1));
            }
        }
         
        //case 1: when the second char of p is not '*', easy case.
        if(p.charAt(1) != '*'){
            if(s.length() < 1){
                return false;
            }
            if((p.charAt(0) != s.charAt(0)) && (p.charAt(0) != '.')){
                return false;
            }
            else{
                return isMatch(s.substring(1), p.substring(1));
            }
        }
         
        //case 2: when the second char of p is '*', complex case.
        else{
             
            //when the '*' stands for 0 preceding element
            if(isMatch(s, p.substring(2))){
                return true;
            }
             
            /*when the '*' stands for 1 or more preceding element,
            try every possible number*/
            int i = 0;
            while(i < s.length() && (s.charAt(i) == p.charAt(0) || p.charAt(0) == '.')){
                if(isMatch(s.substring(i+1), p.substring(2))){
                    return true;
                }
                i++;
            }
            return false;
        }

        
    }
}