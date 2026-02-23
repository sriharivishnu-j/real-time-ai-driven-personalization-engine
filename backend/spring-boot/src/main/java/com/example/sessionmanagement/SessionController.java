package com.example.sessionmanagement;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SessionController {

    @GetMapping("/session")
    public String session() {
        return "Session management service is running";
    }
}