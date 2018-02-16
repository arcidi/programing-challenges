fn main() {
    for x in 1..100{
        let mut out: String = String::new();
        if check_is_fizz(x) {
            out.push_str("Fizz")
        }
        if check_is_buzz(x) {
            out.push_str("Buzz");
        }
        if !check_is_buzz(x) & !check_is_fizz(x) {
            out.push_str(x.to_string().as_str()) // Is there way to convert i32 to &str instead of String?
        }
        println!("{}", out);
    }
}

fn check_is_buzz(x: i32) -> bool {
    if x % 5 == 0 {
        return true;
    }
    return false;
}

fn check_is_fizz(x: i32) -> bool {
    if x % 3 == 0 {
        return true;
    }
    return false;
}