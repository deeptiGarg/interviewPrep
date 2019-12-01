/*Given two strings, base and remove, return a version of the base string where all instances of the remove string have been removed (not case sensitive). You may assume that the remove string is length 1 or more. Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".


withoutString("Hello there", "llo") → "He there"
withoutString("Hello there", "e") → "Hllo thr"
withoutString("Hello there", "x") → "Hello there"
*/


public String withoutString(String base, String remove) {
  int i = 0;
  int match = 0;
  int j;
  StringBuilder str_ret = new StringBuilder();
  while(i<base.length()){
    if(Character.toUpperCase(base.charAt(i)) == Character.toUpperCase(remove.charAt(0))){
      match++;
      if(i+remove.length()-1< base.length()){
          for(j=1 ; j< remove.length(); j++){
          if(Character.toUpperCase(base.charAt(i+j)) == Character.toUpperCase(remove.charAt(j))){
            match++;
          }
          else{
            break;
          }
        }
      }
      if(match==remove.length()){
        i = i+remove.length();
        match = 0;
      }
      else{
        str_ret.append(base.charAt(i));
        i++;
        match = 0;
      }
    }
    else{
      str_ret.append(base.charAt(i));
      i++;
    }
  }
  return str_ret.toString();
}