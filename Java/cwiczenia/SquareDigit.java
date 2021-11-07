public class SquareDigit {
    int outcome;

    public int squareDigits(int n) {
        String x =Integer.toString(n);
        String string_outcome = "";

        for (char c : x.toCharArray()){
            String str = String.valueOf(c);
            int digit = Integer.parseInt(str);

            int result = digit * digit;
            String str_result = String.valueOf(result);

            string_outcome += str_result;
        }

        outcome = Integer.parseInt(string_outcome);
        return outcome;
    }
}