#!/usr/bin/env bash

set -e

ROOT=LegacyTicketTracker

# Create directories
mkdir -p $ROOT/src/main/java/com/company/legacytickettracker/{controller,service,repository,model,dto}
mkdir -p $ROOT/src/main/resources

# pom.xml
cat > $ROOT/pom.xml << 'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0">

<modelVersion>4.0.0</modelVersion>

<groupId>com.company</groupId>
<artifactId>legacy-ticket-tracker</artifactId>
<version>1.0.0</version>
<name>LegacyTicketTracker</name>

<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.2.1</version>
</parent>

<properties>
    <java.version>17</java.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>

    <dependency>
        <groupId>com.h2database</groupId>
        <artifactId>h2</artifactId>
        <scope>runtime</scope>
    </dependency>
</dependencies>

</project>
EOF

# Application
cat > $ROOT/src/main/java/com/company/legacytickettracker/LegacyTicketTrackerApplication.java << 'EOF'
package com.company.legacytickettracker;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class LegacyTicketTrackerApplication {

    public static void main(String[] args) {
        SpringApplication.run(LegacyTicketTrackerApplication.class, args);
    }
}
EOF

# TicketStatus
cat > $ROOT/src/main/java/com/company/legacytickettracker/model/TicketStatus.java << 'EOF'
package com.company.legacytickettracker.model;

public enum TicketStatus {
    OPEN,
    IN_PROGRESS,
    CLOSED
}
EOF

# Ticket
cat > $ROOT/src/main/java/com/company/legacytickettracker/model/Ticket.java << 'EOF'
package com.company.legacytickettracker.model;

import jakarta.persistence.*;
import java.util.List;

@Entity
public class Ticket {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;
    private String description;

    @Enumerated(EnumType.STRING)
    private TicketStatus status = TicketStatus.OPEN;

    @OneToMany(mappedBy = "ticket", cascade = CascadeType.ALL)
    private List<Comment> comments;

    public Long getId() { return id; }
    public String getTitle() { return title; }
    public String getDescription() { return description; }
    public TicketStatus getStatus() { return status; }

    public void setTitle(String title) { this.title = title; }
    public void setDescription(String description) { this.description = description; }
    public void setStatus(TicketStatus status) { this.status = status; }
}
EOF

# Comment
cat > $ROOT/src/main/java/com/company/legacytickettracker/model/Comment.java << 'EOF'
package com.company.legacytickettracker.model;

import jakarta.persistence.*;

@Entity
public class Comment {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String message;

    @ManyToOne
    private Ticket ticket;

    public Long getId() { return id; }
    public String getMessage() { return message; }

    public void setMessage(String message) { this.message = message; }
    public void setTicket(Ticket ticket) { this.ticket = ticket; }
}
EOF

# Repositories
cat > $ROOT/src/main/java/com/company/legacytickettracker/repository/TicketRepository.java << 'EOF'
package com.company.legacytickettracker.repository;

import com.company.legacytickettracker.model.Ticket;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TicketRepository extends JpaRepository<Ticket, Long> {
}
EOF

cat > $ROOT/src/main/java/com/company/legacytickettracker/repository/CommentRepository.java << 'EOF'
package com.company.legacytickettracker.repository;

import com.company.legacytickettracker.model.Comment;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CommentRepository extends JpaRepository<Comment, Long> {
}
EOF

# Services
cat > $ROOT/src/main/java/com/company/legacytickettracker/service/TicketService.java << 'EOF'
package com.company.legacytickettracker.service;

import com.company.legacytickettracker.model.Ticket;
import com.company.legacytickettracker.model.TicketStatus;
import com.company.legacytickettracker.repository.TicketRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TicketService {

    private final TicketRepository repo;

    public TicketService(TicketRepository repo) {
        this.repo = repo;
    }

    public List<Ticket> getAll() {
        return repo.findAll();
    }

    public Ticket create(Ticket t) {
        return repo.save(t);
    }

    public Ticket updateStatus(Long id, TicketStatus status) {
        Ticket ticket = repo.findById(id).orElse(null);
        if (ticket == null) return null;

        ticket.setStatus(status);
        return repo.save(ticket);
    }
}
EOF

cat > $ROOT/src/main/java/com/company/legacytickettracker/service/CommentService.java << 'EOF'
package com.company.legacytickettracker.service;

import com.company.legacytickettracker.model.Comment;
import com.company.legacytickettracker.repository.CommentRepository;
import org.springframework.stereotype.Service;

@Service
public class CommentService {

    private final CommentRepository repo;

    public CommentService(CommentRepository repo) {
        this.repo = repo;
    }

    public Comment create(Comment c) {
        return repo.save(c);
    }
}
EOF

# Controllers
cat > $ROOT/src/main/java/com/company/legacytickettracker/controller/TicketController.java << 'EOF'
package com.company.legacytickettracker.controller;

import com.company.legacytickettracker.model.Ticket;
import com.company.legacytickettracker.model.TicketStatus;
import com.company.legacytickettracker.service.TicketService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/tickets")
public class TicketController {

    private final TicketService service;

    public TicketController(TicketService service) {
        this.service = service;
    }

    @GetMapping
    public List<Ticket> getAll() {
        return service.getAll();
    }

    @PostMapping
    public Ticket create(@RequestBody Ticket t) {
        return service.create(t);
    }

    @PutMapping("/{id}/status")
    public Ticket updateStatus(@PathVariable Long id,
                               @RequestParam TicketStatus status) {
        return service.updateStatus(id, status);
    }
}
EOF

cat > $ROOT/src/main/java/com/company/legacytickettracker/controller/CommentController.java << 'EOF'
package com.company.legacytickettracker.controller;

import com.company.legacytickettracker.model.Comment;
import com.company.legacytickettracker.service.CommentService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/comments")
public class CommentController {

    private final CommentService service;

    public CommentController(CommentService service) {
        this.service = service;
    }

    @PostMapping
    public Comment create(@RequestBody Comment c) {
        return service.create(c);
    }
}
EOF

# DTO (placeholder)
cat > $ROOT/src/main/java/com/company/legacytickettracker/dto/TicketRequest.java << 'EOF'
package com.company.legacytickettracker.dto;

public class TicketRequest {
    public String title;
    public String description;
}
EOF

# application.properties
cat > $ROOT/src/main/resources/application.properties << 'EOF'
spring.datasource.url=jdbc:h2:mem:testdb
spring.jpa.hibernate.ddl-auto=update
spring.h2.console.enabled=true
EOF

echo "✅ LegacyTicketTracker created successfully."
