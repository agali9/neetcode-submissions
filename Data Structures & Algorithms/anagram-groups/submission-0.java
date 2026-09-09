class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> arr = new HashMap<>();
        for(int i=0;i<strs.length;i++){
            char[] c = strs[i].toCharArray();
            Arrays.sort(c);
            String nstr = String.valueOf(c);
            arr.putIfAbsent(nstr, new ArrayList<>());
            arr.get(nstr).add(strs[i]);
        }
        return new ArrayList<>(arr.values());
    }
}
