package com.app.week7.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class PostController
{
    @PostMapping("/post")
    public @ResponseBody
    String write(Model model, @RequestParam("content") String content) throws Exception
    {
        model.addAttribute("content", content);
        String a = content;
        System.out.println(a);
        return a;
    }

    @GetMapping("/post")
    public @ResponseBody String show(Model model) throws Exception
    {
        String content = (String) model.getAttribute("content");

        return content;
    }
}
