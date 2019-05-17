package solution

func removeOuterParentheses(S string) string {
    c := 0
    r := ""
    for _, rune := range S {
        if rune == '(' {
            c++
            if c > 1 {
                r += string(rune)
            }
            continue
        } else {
            c--
            if c > 0 {
                r += string(rune)
            }
            continue
        }
    }
    return r
}