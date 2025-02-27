import { Button, Text, Linking, View } from "react-native";

export default function Index() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
      }}
    >
      <Text>Hypertension PDF (v2)</Text>
      <Button
        onPress={() => {
          Linking.openURL("https://s3.af-south-1.amazonaws.com/shayela-backend/articles/Hypertension_A5Flyer_GuudDrivers_2024.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAVVKHTEX6ICOCXE25%2F20241031%2Faf-south-1%2Fs3%2Faws4_request&X-Amz-Date=20241031T200646Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCmFmLXNvdXRoLTEiSDBGAiEAm6ZVTFJYlZLwTzA6gXy8n28tKlXFCHcG0eIf%2FCrZhGUCIQC5b5kegdllZBkqquoYY%2B7OKaGYmqk%2BIxBGOMNTpqnt5Sq%2FBQiV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDM4OTM4MTU2MzkwMCIM7Cy0yHVn72ipE1IlKpMFNlgcymXg8FpLvZpzc5LqJXbFpuXbYI%2FkuxN6MK8sc8mUiZ7yYReaAf7BNKOXh1G4bWu8N1rahphpWIw%2BDtI0eUKti0uw4kZCBQ1uFHuDMNeL87EG%2FtvILVa2O1NW%2BjUwMZTqm4ekGZYxlP1%2Fy%2F%2BhKPGJVnvdCSGdzO9xeykkgEXRSdjVcoZrdzGjr%2BauuVDtOdUHdRq%2FhXaGj1aGSaHzpecZ%2BqNBqZrFscnCvsLKasoVVZEYpqVC5WotxN9acA2IKb7Q54Nen4M9HA0mZp%2BXeIxosbuWhh1CWpRWGc953G%2F6jJiQ7juq5uUpWBwcj9SkR3VMd0nG%2FUpPrnMHaNjMyBhQeDLVZYyltNDUHHB4Jpnf1wkbO4wc8AIE9lCt49rRumR6xbTbUThYDFbKvgV%2FZBt93RR6M6I4KqtWmPLjApvfRfFnapFTV6tiRqcrX1iRSO%2F4%2Bim5rEL4RcD%2BzBsMw%2FpJWFmoRL43zqX96j64sJYEPXSyGpQlQ43oEn1udJ%2BJwqJs2imXPauUtySKCoyPjjgaP3S7ho7jdKxUw6xyIkvrd5sRdH%2BcJX%2FCAVyVKQ5pJQYmdScR4tcUErKOqETmZoQUWd4ed%2FobN%2BtsUJmhfGjj2fItfN9dnXHevl4W%2FO%2B8DfSqXUcK0NjVv1vRr3ramqfLFy0yjRzlxiZt0o51YaeIpQCe4g%2FRJm7kKLCWuQfTqXOKgUC9%2Faw9Ma7wY4feSXypBMt67KTwBNQj3EInlFWDWAaOyED9tf3FirQKRL1PWGBTAwNjH2QAcF5pe5RxLxXp0AMCkCvKzjsnF8ZlJNXqhpz8nf64gEuLA1A4NhQArulnHPjjKvooXk%2F4E1Vk6N%2FkxcO0JNCpJ9rVGbjirz9nYNQwt7iPuQY6sAHJp9xpJD3pEaZJ%2FNtIwk%2BI6DudoxhXs4Cs%2FEm0en9ONXaencpaIqMkHeCE5fOAG69XJtgcw0152wErRL5PMcZa6i%2F%2BjguqfxKsnWtTD4KBLmrDfK9vBx3uDf44xoLtSbW0F8YlgyIJSEIKPCzsPEndbHsW0IzJFOtaS4YAFppEMnho3pAwGo8xYdr3c%2FL812z00LrLgMs4j8TRmWgIuxlmQb%2BgVKiVYEMCE2uTAdb0eQ%3D%3D&X-Amz-Signature=55bca88ea494ec0ade903d9cdbac9f57df72f51ad6fb88b39e8015e9339f8908")
        }}
        title="Show"
      />
    </View>
  );
}
