package com.app.week7.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.List;

@Controller
public class PostController
{
    @PostMapping("/post")
    public @ResponseBody
    String write(HttpServletRequest request, @RequestParam("content") String content) throws Exception
    {
        HttpSession session = request.getSession();
        session.setAttribute("content",content);

//        model.addAttribute("content", content);
        String a = content;
        System.out.println(a);
        return a;
    }

    @GetMapping("/post")
    public @ResponseBody String show(HttpServletRequest request) throws Exception
    {
        HttpSession session = request.getSession();
        String content = (String) session.getAttribute("content");
        System.out.println(content);
        return content;
    }
}
