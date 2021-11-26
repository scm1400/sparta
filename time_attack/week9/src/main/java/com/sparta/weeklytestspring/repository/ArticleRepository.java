package com.sparta.weeklytestspring.repository;

import com.sparta.weeklytestspring.domain.Article;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ArticleRepository extends JpaRepository<Article, Long> {
    List<Article> findByTags(String tag);
}
