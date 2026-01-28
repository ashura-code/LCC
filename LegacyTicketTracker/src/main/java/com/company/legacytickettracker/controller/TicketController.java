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
