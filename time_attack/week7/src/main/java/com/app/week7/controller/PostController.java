package com.app.week7.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
public class PostController
{
    @PostMapping("/post")
    public String write(Model model, @RequestParam("content") String content) throws Exception
    {
        System.out.println(content);
        return "redirect:/";
    }
}
